from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/user-register",
        view=views.UserRegisterAPIView.as_view(),
        name="api-v1-user-register",
    ),
    path(
        route="api/v1/user-login",
        view=views.UserLoginAPIView.as_view(),
        name="api-1-user-login",
    ),
    path(
        route="api/v1/user-logout",
        view=views.UserLogoutAPIView.as_view(),
        name="api-v1-user-logout",
    ),
    path(
        route="api/v1/accounts",
        view=views.UsersAPIView.as_view(),
        name="api-v1-users",
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
