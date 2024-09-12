from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/shop/add-to-wishlist",
        view=views.AddOrRemoveFromWishlistAPIView.as_view(),
        name="api-v1-shop-add-to-wishlist",
    ),
]
