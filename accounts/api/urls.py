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
        view=views.UserLoginAPIView.as_view(),
        name="api-v1-accounts-account-login",
    ),
    path(
        route="activate/<uidb64>/<token>",
        view=views.activate,
        name="activate",
    ),
    path(
        route="log-out",
        view=views.UserLogoutAPIView.as_view(),
        name="logout",
    ),
    path(
        route="api/v1/accounts/forgot-password",
        view=views.ForgotPasswordAPIView.as_view(),
        name="api-v1-accounts-forgot-password",
    ),
    path(
        route="api/v1/accounts/update-account",
        view=views.UserUpdateAPIView.as_view(),
        name="api-v1-accounts-update-account",
    ),
    path(
        route="api/v1/profiles/update-profile",
        view=views.ProfileUpdateAPIView.as_view(),
        name="api-v1-profiles-update-profile"
    ),
    path(
        route="api/v1/profiles/delete-profile-picture",
        view=views.ProfileDeleteAPIView.as_view(),
        name="api-v1-profiles-delete-profile-picture",
    ),
]
