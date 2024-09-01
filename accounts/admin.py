from django.contrib import admin
from .models import User, Profile, OneTimePassword, DeliveryDetails, ProfilePicture
from .forms import UserForm, ProfileForm, OneTimePasswordForm, DeliveryDetailsForm, ProfilePictureForm
from django.contrib.sessions.models import Session
from django.utils.html import format_html


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


@admin.register(OneTimePassword)
class AdminOneTimePassword(admin.ModelAdmin):
    """
    Admin options and functionalities for OneTimePassword model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "user",
        "uuid"
    ]
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

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"


@admin.register(ProfilePicture)
class AdminProfilePicture(admin.ModelAdmin):
    """
    Admin options and functionalities for ProfilePicture model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "formatted_updated_at",
        "image",
        "formatted_image_name",
        "size",
        "width",
        "height",
        "format",
        "alt",
    ]
    form = ProfilePictureForm
    fieldsets = (
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
    )

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def formatted_updated_at(self, obj):
        return obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_updated_at.short_description = "Updated At"

    def formatted_image_name(self, obj):
        if obj.image:
            return obj.image.name.split("/")[-1]

    formatted_image_name.short_description = "Image Name"


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    """
    Admin options and functionalities for Profile model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "get_user_id",
        "user",
        "get_first_name",
        "get_last_name",
        "get_profilepicture_id",
        "get_profilepicture",
        "bio",
        "gender",
        "formatted_date_of_birth",
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
                    "gender",
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

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def get_user_id(self, obj):
        return obj.user.id

    get_user_id.short_description = "User ID"

    def get_first_name(self, obj):
        return obj.firstname

    get_first_name.short_description = "First Name"

    def get_last_name(self, obj):
        return obj.lastname

    get_last_name.short_description = "Last Name"

    def get_profilepicture_id(self, obj):
        if obj.profilepicture:
            return obj.profilepicture

    get_profilepicture_id.short_description = "Profile Picture ID"

    def get_profilepicture(self, obj):
        if obj.profilepicture:
            return obj.profilepicture.image

    get_profilepicture.short_description = "Profile Picture"

    def formatted_date_of_birth(self, obj):
        if obj.dateofbirth:
            return obj.dateofbirth.strftime("%Y-%m-%d")

    formatted_date_of_birth.short_description = "Date of Birth"


@admin.register(DeliveryDetails)
class AdminDeliveryDetails(admin.ModelAdmin):
    """
    Admin options and functionalities for DeliveryDetails model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "get_profile_id",
        "get_profile",
        "country",
        "state",
        "city",
        "street",
        "get_house_number",
        "get_apartment_number",
        "get_postal_code",
        "phone",
    ]
    form = DeliveryDetailsForm
    fieldsets = (
        (
            "Contact Information", {
                "fields": [
                    "phone",
                ],
            },
        ),
        (
            "Shipping Address", {
                "fields": [
                    "country",
                    "state",
                    "city",
                    "street",
                    "housenumber",
                    "apartmentnumber",
                    "postalcode",
                ],
            },
        ),
    )

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def get_profile_id(self, obj):
        return obj.profile.id

    get_profile_id.short_description = "Profile ID"

    def get_profile(self, obj):
        return obj.profile

    get_profile.short_description = "Profile"

    def get_house_number(self, obj):
        return obj.housenumber

    get_house_number.short_description = "House Number"

    def get_apartment_number(self, obj):
        return obj.apartmentnumber

    get_apartment_number.short_description = "Apartment Number"

    def get_postal_code(self, obj):
        return obj.postalcode

    get_postal_code.short_description = "Postal Code"


@admin.register(Session)
class AdminSession(admin.ModelAdmin):
    list_display = ["session_key", "_session_data", "expire_date"]

    def _session_data(self, obj):
        return obj.get_decoded()
