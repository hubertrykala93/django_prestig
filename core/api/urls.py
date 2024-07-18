from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/newsletters",
        view=views.NewsletterAPIView.as_view(),
        name="api-v1-newsletters",
    ),
    path(
        route="api/v1/newsletters/<int:pk>",
        view=views.NewsletterRetrieveAPIView.as_view(),
        name="api-v1-newsletters-newsletter-details",
    ),
    path(
        route="api/v1/newsletters/create",
        view=views.NewsletterCreateAPIView.as_view(),
        name="api-v1-newsletters-create",
    ),
    path(
        route="api/v1/newsletters/update/<int:pk>",
        view=views.NewsletterUpdateAPIView.as_view(),
        name="api-v1-newsletters-update",
    ),
    path(
        route="api/v1/newsletters/delete/<int:pk>",
        view=views.NewsletterDeleteAPIView.as_view(),
        name="api-v1-newsletters-delete",
    ),
]
