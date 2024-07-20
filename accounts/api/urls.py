from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/users",
        view=views.UsersAPIView.as_view(),
        name="api-v1-users",
    ),
    path(
        route="api/v1/users/<int:pk>",
        view=views.UserRetrieveAPIView.as_view(),
        name="api-v1-users-user-details-by-id",
    ),
    path(
        route="api/v1/users/<str:username>",
        view=views.UserRetrieveAPIView.as_view(),
        name="api-v1-users-user-details-by-username",
    ),
]
