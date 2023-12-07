from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.username", read_only=True)
    friend = serializers.CharField(source="friend.username", read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "name", "friend", "has_selected", "has_been_selected")
