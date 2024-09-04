from django.urls import path
from . import views as shop_views

urlpatterns = [
    path(route="shop", view=shop_views.shop, name="shop"),
    path(route="shop/category/<slug:category_slug>", view=shop_views.products_by_category, name="products-by-category"),
    path(route="shop/subcategory/<slug:subcategory_slug>", view=shop_views.products_by_subcategory,
         name="products-by-subcategory"),
    path(route="shop/tag/<slug:tag_slug>", view=shop_views.products_by_tag, name="products-by-tag"),
    path(route="shop/<slug:category_slug>/<slug:subcategory_slug>/<slug:product_slug>", view=shop_views.product_details,
         name="product-details"),
]
