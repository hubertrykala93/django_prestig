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
    list_display = [
        "id",
        "formatted_created_at",
        "email"
    ]
    form = NewsletterForm
    fieldsets = (
        (
            "Subscriber", {
                "fields": ["email"],
            },
        ),
    )

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"


@admin.register(ContactMail)
class AdminContactMail(admin.ModelAdmin):
    """
    Admin options and functionalities for ContactMail model.
    """
    list_display = [
        "id",
        "formatted_date_sent",
        "get_full_name",
        "email",
        "subject",
        "message"
    ]
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

    def get_full_name(self, obj):
        return obj.fullname

    get_full_name.short_description = "Full Name"

    def formatted_date_sent(self, obj):
        return obj.date_sent.strftime("%Y-%m-%d %H:%M:%S")

    formatted_date_sent.short_description = "Date Sent"
