# example/views.py
from datetime import datetime

from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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
