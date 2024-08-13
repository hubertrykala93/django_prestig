from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/delivery-details/update-delivery-details",
        view=views.DeliveryDetailsUpdateAPIView.as_view(),
        name="api-v1-delivery-details-update-delivery-details",
    ),
]
