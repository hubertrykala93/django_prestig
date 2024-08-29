from django.contrib import admin
from .models import User, Profile, OneTimePassword, DeliveryDetails, ProfilePicture
from .forms import UserForm, ProfileForm, OneTimePasswordForm, DeliveryDetailsForm, ProfilePictureForm
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
        "created_at",
        "updated_at",
        "image",
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
        (
            "Alt Text", {
                "fields": [
                    "alt",
                ],
            },
        ),
    )


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    """
    Admin options and functionalities for Profile model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "user",
        "get_first_name",
        "get_last_name",
        "bio",
        "gender",
        "formatted_date_of_birth",
        "get_profilepicture_id",
        "get_profilepicture_name",
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

    def get_first_name(self, obj):
        return obj.firstname

    get_first_name.short_description = "First Name"

    def get_last_name(self, obj):
        return obj.lastname

    get_last_name.short_description = "Last Name"

    def formatted_date_of_birth(self, obj):
        if obj.dateofbirth:
            return obj.dateofbirth.strftime("%Y-%m-%d")

    formatted_date_of_birth.short_description = "Date of Birth"

    def get_profilepicture_id(self, obj):
        if obj.profilepicture:
            return obj.profilepicture.id

    get_profilepicture_id.short_description = "Profile Picture ID"

    def get_profilepicture_name(self, obj):
        if obj.profilepicture:
            return obj.profilepicture.image.name.split("/")[-1]

    get_profilepicture_name.short_description = "Profile Picture Name"


@admin.register(DeliveryDetails)
class AdminDeliveryDetails(admin.ModelAdmin):
    """
    Admin options and functionalities for DeliveryDetails model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "uuid",
        "country",
        "state",
        "city",
        "street",
        "get_house_number",
        "get_apartment_number",
        "get_postal_code",
        "phone",
        "get_username",
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

    def get_house_number(self, obj):
        return obj.housenumber

    get_house_number.short_description = "House Number"

    def get_apartment_number(self, obj):
        return obj.apartmentnumber

    get_apartment_number.short_description = "Apartment Number"

    def get_postal_code(self, obj):
        return obj.postalcode

    get_postal_code.short_description = "Postal Code"

    def get_username(self, obj):
        return obj.profile

    get_username.short_description = "Username"


@admin.register(Session)
class AdminSession(admin.ModelAdmin):
    list_display = ["session_key", "_session_data", "expire_date"]

    def _session_data(self, obj):
        return obj.get_decoded()
