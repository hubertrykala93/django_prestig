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
        name="api-1-accounts-account-login",
    ),
    path(
        route="api/v1/accounts/account-logout",
        view=views.UserLogoutAPIView.as_view(),
        name="api-v1-accounts-account-logout",
    ),
    path(
        route="api/v1/accounts",
        view=views.UsersAPIView.as_view(),
        name="api-v1-accounts",
    ),
    path(
        route="api/v1/accounts/<int:pk>",
        view=views.UserRetrieveAPIView.as_view(),
        name="api-v1-accounts-account-details-by-id",
    ),
    path(
        route="api/v1/accounts/<str:username>",
        view=views.UserRetrieveAPIView.as_view(),
        name="api-v1-accounts-account-details-by-username",
    ),
    path(
        route="api/v1/accounts/delete/<int:pk>",
        view=views.UserDeleteAPIView.as_view(),
        name="api-v1-accounts-account-delete",
    ),
]
