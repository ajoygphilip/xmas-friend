from django.contrib import admin

from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "get_user_name",
        "get_friend_name",
        "has_selected",
        "has_been_selected",
    )

    def get_user_name(self, obj):
        return obj.user.username if obj.user else f"User {obj.user.username}"

    def get_friend_name(self, obj):
        return obj.friend.username if obj.friend else False

    get_user_name.short_description = "User "
    get_friend_name.short_description = "Friend "


admin.site.register(Profile, ProfileAdmin)
