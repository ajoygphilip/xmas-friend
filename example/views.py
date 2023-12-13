from datetime import datetime

from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user.profile.id)
        print(self.request.user.profile.has_been_selected)
        if self.request.user.is_authenticated:
            return (
                Profile.objects.filter(friend=None)
                .exclude(user=self.request.user)
                .filter(friend=None)
            )
        else:
            return Profile.objects.filter(friend=None)

    def list(self, request, *args, **kwargs):
        user = request.user
        print(user.username)
        if user.profile.has_selected:
            return Response(
                {
                    "message": "you have already selected a friend",
                    "friend": user.profile.friend.username,
                }
            )
        else:
            return super().list(request, *args, **kwargs)

    @action(detail=False, methods=["post"])
    def set_friend(self, request):
        friend_id = request.data.get("friend_id")

        print("user =", request.user.id)
        print("friend =", friend_id)

        if not friend_id:
            return Response({"error": "friend_id is required"}, status=400)

        if friend_id == request.user.id:
            return Response({"error": "you cannot be your own friend"}, status=400)

        try:
            friend_id = int(friend_id)
            friend_profile = Profile.objects.get(id=friend_id)
        except Profile.DoesNotExist:
            return Response({"error": "Friend profile not found"}, status=404)

        current_user_profile = request.user.profile
        current_user_profile.friend = friend_profile.user
        current_user_profile.has_selected = True
        current_user_profile.save()

        friend_profile.has_been_selected = True
        friend_profile.save()

        return Response({"success": "Friend set successfully"}, status=200)
