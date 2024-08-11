from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/deliveries/delivery-details/<int:pk>",
        view=views.DeliveryDetailsDetailsAPIView.as_view(),
        name="api-v1-deliveries-delivery-details",
    ),
]
