# example/urls.py
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from example.views import SampleView, index

from .views import ProfileViewset, logout_view

urlpatterns = [
    path("", index),
    path("test/", SampleView.as_view(), name="my-api"),
    path("login/", obtain_auth_token, name="login"),
]

router = routers.SimpleRouter()
router.register("profiles", ProfileViewset, basename="accounts")
urlpatterns += router.urls
