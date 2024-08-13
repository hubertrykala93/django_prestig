from django.contrib import admin
from .models import User, Profile
from .forms import UserForm, ProfileForm
from django.contrib.sessions.models import Session


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    """
    Admin options and functionalities for User model.
    """
    list_display = ["id", "username", "email", "is_verified", "is_active", "is_staff", "is_superuser",
                    "date_joined",
                    "last_login"]
    list_editable = ["username", "email", "is_verified"]
    form = UserForm
    fieldsets = (
        (
            "Basic Informations", {
                "fields": [
                    "username",
                    "email",
                    "password",
                ],
            },
        ),
        (
            "Permissions", {
                "fields": [
                    "is_verified",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ],
            },
        ),
    )


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    """
    Admin options and functionalities for Profile model.
    """
    list_display = ["id", "user", "firstname", "lastname", "bio", "gender", "dateofbirth", "profilepicture", "facebook",
                    "instagram", "delivery_details"]
    form = ProfileForm
    fieldsets = (
        (
            "Basic Informations", {
                "fields": [
                    "user",
                    "firstname",
                    "lastname",
                    "bio",
                    "date_of_birth",
                ],
            },
        ),
        (
            "Uploading", {
                "fields": [
                    "profile_picture",
                ],
            },
        ),
        (
            "Social Media", {
                "fields": [
                    "facebook_username",
                    "instagram_username",
                ],
            },
        ),
        (
            "Favorite Products", {
                "fields": [
                    "wishlist",
                ],
            },
        ),
        (
            "Delivery Informations", {
                "fields": [
                    "delivery_details",
                ],
            },
        ),
    )


@admin.register(Session)
class AdminSession(admin.ModelAdmin):
    list_display = ["session_key", "_session_data", "expire_date"]

    def _session_data(self, obj):
        return obj.get_decoded()
