from django.contrib import admin
from .forms import NewsletterForm
from .models import Newsletter


@admin.register(Newsletter)
class AdminNewsletter(admin.ModelAdmin):
    """
    Admin options and functionalities for Newsletter model.
    """
    fields = ["email"]
    list_display = ["id", "created_at", "email"]
    form = NewsletterForm
