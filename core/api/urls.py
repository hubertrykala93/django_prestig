from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1",
        view=views.api_endpoints,
        name="api-endpoints",
    ),
    path(
        route="api/v1/newsletters",
        view=views.NewslettersAPIView.as_view(),
        name="api-v1-newsletters",
    ),
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
