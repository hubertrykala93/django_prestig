from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/accounts/account-register",
        view=views.UserRegisterAPIView.as_view(),
        name="api-v1-accounts-account-register",
    ),
    path(
        route="api/v1/accounts/account-login",
        view=views.UserLoginAPIView().as_view(),
        name="api-v1-accounts-account-login",
    ),
    path(
        route="activate/<uidb64>/<token>", view=views.activate, name="activate",
    )
]
