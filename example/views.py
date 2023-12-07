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
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
