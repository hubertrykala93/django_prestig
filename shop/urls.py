from django.urls import path
from . import views as shop_views

urlpatterns = [
    path(route="shop", view=shop_views.shop, name="shop"),
    path(route="shop/<slug:category_slug>", view=shop_views.products_by_category, name="products-by-category"),
    path(route="shop/<slug:category_slug>/<slug:subcategory_slug>", view=shop_views.products_by_subcategory,
         name="products-by-subcategory"),
    path(route="shop/tag/<slug:tag_slug>", view=shop_views.products_by_tag, name="products-by-tag"),
]
