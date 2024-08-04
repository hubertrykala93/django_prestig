from django.urls import path
from . import views as shop_views

urlpatterns = [
    path(route="shop", view=shop_views.shop, name="shop"),
]
