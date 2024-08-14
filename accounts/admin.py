from django.contrib import admin
from .models import User, Profile, OneTimePassword
from .forms import UserForm, ProfileForm, OneTimePasswordForm
from django.contrib.sessions.models import Session


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    """
    Admin options and functionalities for User model.
    """
    list_display = [
        "id",
        "formatted_date_joined",
        "username",
        "email",
        "is_verified",
        "is_active",
        "is_staff",
        "is_superuser",
        "formatted_last_login"
    ]
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

    def formatted_date_joined(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d %H:%M:%S")

    formatted_date_joined.short_description = "Date Joined"

    def formatted_last_login(self, obj):
        if obj.last_login:
            return obj.last_login.strftime("%Y-%m-%d %H:%M:%S")

    formatted_last_login.short_description = "Last Login"


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    """
    Admin options and functionalities for Profile model.
    """
    list_display = [
        "id",
        "user",
        "get_first_name",
        "get_last_name",
        "bio",
        "gender",
        "formatted_date_of_birth",
        "formatted_profile_picture",
        "facebook",
        "instagram",
        "delivery_details"
    ]
    form = ProfileForm
    fieldsets = (
        (
            "Basic Informations", {
                "fields": [
                    "user",
                    "firstname",
                    "lastname",
                    "bio",
                    "dateofbirth",
                ],
            },
        ),
        (
            "Uploading", {
                "fields": [
                    "profilepicture",
                ],
            },
        ),
        (
            "Social Media", {
                "fields": [
                    "facebook",
                    "instagram",
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

    def get_first_name(self, obj):
        return obj.firstname

    get_first_name.short_description = "First Name"

    def get_last_name(self, obj):
        return obj.lastname

    get_last_name.short_description = "Last Name"

    def get_profile_picture(self, obj):
        return obj.profilepicture

    get_profile_picture.short_description = "Profile Picture"

    def formatted_date_of_birth(self, obj):
        if obj.dateofbirth:
            return obj.dateofbirth.strftime("%Y-%m-%d")

    formatted_date_of_birth.short_description = "Date of Birth"

    def formatted_profile_picture(self, obj):
        return obj.profilepicture.name.split(sep="/")[-1]

    formatted_profile_picture.short_description = "Profile Picture"


@admin.register(OneTimePassword)
class AdminOneTimePassword(admin.ModelAdmin):
    """
    Admin options and functionalities for OneTimePassword model.
    """
    list_display = ["id", "user", "uuid"]
    form = OneTimePasswordForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "user",
                ],
            },
        ),
    )


@admin.register(Session)
class AdminSession(admin.ModelAdmin):
    list_display = ["session_key", "_session_data", "expire_date"]

    def _session_data(self, obj):
        return obj.get_decoded()
