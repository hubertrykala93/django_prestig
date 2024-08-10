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
    list_display = ["id", "created_at", "email"]
    form = NewsletterForm
    fieldsets = (
        (
            "Subscriber", {
                "fields": ["email"],
            },
        ),
    )


@admin.register(ContactMail)
class AdminContactMail(admin.ModelAdmin):
    """
    Admin options and functionalities for ContactMail model.
    """
    list_display = ["id", "date_sent", "fullname", "email", "subject", "message"]
    form = ContactMailForm
    fieldsets = (
        (
            "Contact Information", {
                "fields": [
                    "fullname",
                    "email",
                ],
            },
        ),
        (
            "Message Content", {
                "fields": [
                    "subject",
                    "message",
                ]
            }
        )
    )
