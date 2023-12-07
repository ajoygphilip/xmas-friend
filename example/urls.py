# example/urls.py
from django.urls import path

from example.views import SampleView, index

urlpatterns = [
    path("", index),
    path("test/", SampleView.as_view(), name="my-api"),
]
