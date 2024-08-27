from django.urls import path
from . import views as accounts_views

urlpatterns = [
    path(route="register", view=accounts_views.register, name="register"),
    path(route="login", view=accounts_views.login, name="login"),
    path(route="change-password", view=accounts_views.change_password, name="change-password"),
    path(route="forgot-password", view=accounts_views.forgot_password, name="forgot-password"),
    path(route="profile/<str:username>", view=accounts_views.profile_page, name="profile"),
    path(route="my-account", view=accounts_views.my_account, name="my-account"),
    path(route="my-account/account-settings", view=accounts_views.account_settings, name="account-settings"),
    path(route="my-account/profile-settings", view=accounts_views.profile_settings, name="profile-settings"),
    path(route="my-account/comments-summary", view=accounts_views.comments_summary, name="comments-summary"),
    path(route="my-account/delivery-details", view=accounts_views.delivery_details, name="delivery-details"),
    path(route="my-account/purchased-products", view=accounts_views.purchased_products, name="purchased-products"),
    path(route="my-account/product-returns", view=accounts_views.product_returns, name="product-returns"),
    path(route="my-account/product-reviews", view=accounts_views.product_reviews, name="product-reviews"),
]
