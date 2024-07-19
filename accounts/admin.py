from django.contrib import admin
from .models import User
from .forms import UserForm


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    """
    Admin options and functionalities for Brand model.
    """
    fields = ["username", "email", "password", "is_verified", "is_active", "is_staff", "is_superuser"]
    list_display = ["id", "username", "email", "is_verified", "is_active", "is_staff", "is_superuser", "date_joined",
                    "last_login"]
    list_editable = ["username", "email", "is_verified"]
    form = UserForm
