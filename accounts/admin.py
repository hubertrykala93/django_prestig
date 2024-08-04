from django.contrib import admin
from .models import User, Profile
from .forms import UserForm
from django.contrib.sessions.models import Session

admin.site.register(Profile)


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    """
    Admin options and functionalities for Brand model.
    """
    fields = ["username", "email", "password", "is_verified", "is_active", "is_staff", "is_superuser"]
    list_display = ["id", "username", "email", "is_verified", "is_active", "is_staff", "is_superuser",
                    "date_joined",
                    "last_login"]
    list_editable = ["username", "email", "is_verified"]
    form = UserForm


@admin.register(Session)
class AdminSession(admin.ModelAdmin):
    list_display = ["session_key", "_session_data", "expire_date"]

    def _session_data(self, obj):
        return obj.get_decoded()
