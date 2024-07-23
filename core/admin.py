from django.contrib import admin
from .forms import NewsletterForm, ContactMailForm
from .models import Newsletter, ContactMail
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(Newsletter)
class AdminNewsletter(admin.ModelAdmin):
    """
    Admin options and functionalities for Newsletter model.
    """
    fields = ["email"]
    list_display = ["id", "created_at", "email"]
    form = NewsletterForm


@admin.register(ContactMail)
class AdminContactMail(admin.ModelAdmin):
    """
    Admin options and functionalities for ContactMail model.
    """
    fields = ["fullname", "email", "subject", "message"]
    list_display = ["id", "date_sent", "fullname", "email", "subject", "message"]
    form = ContactMailForm
