from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/newsletters/create",
        view=views.NewsletterCreateAPIView.as_view(),
        name="api-v1-newsletters-create",
    ),
    path(
        route="api/v1/contact-mails/create",
        view=views.ContactMailCreateAPIView.as_view(),
        name="api-v1-contact-mails-create",
    ),
]
