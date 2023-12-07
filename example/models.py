from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    friend = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None, related_name="friend", null=True
    )
    has_selected = models.BooleanField(default=False)
    has_been_selected = models.BooleanField(default=False)
