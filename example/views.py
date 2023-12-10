from datetime import datetime

from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer


def index(request):
    now = datetime.now()
    html = f"""
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    """
    return HttpResponse(html)


class SampleView(APIView):
    def get(self, request, *args, **kwargs):
        data = {"message": "Success! GET request handled successfully."}
        return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Profile.objects.filter(friend=None).exclude(user=self.request.user)
        else:
            return Profile.objects.filter(friend=None)

    @action(detail=True, methods=["post"])
    def setFriend(self, request):
        friend_id = request.data.get("friend_id")

        if not friend_id:
            return Response({"error": "friend_id is required"}, status=400)

        try:
            friend_profile = Profile.objects.get(user__id=friend_id)
        except Profile.DoesNotExist:
            return Response({"error": "Friend profile not found"}, status=404)

        current_user_profile = self.get_queryset().get(user=request.user)

        current_user_profile.friend = friend_profile
        current_user_profile.save()

        return Response({"success": "Friend set successfully"}, status=200)
