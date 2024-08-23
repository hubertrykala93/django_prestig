from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/comments/create-comment",
        view=views.CommentCreateAPIView.as_view(),
        name="api-v1-comments-create-comment",
    ),
    path(
        route="api/v1/comments/edit-comment",
        view=views.CommentUpdateAPIView.as_view(),
        name="api-v1-comments-edit-comment",
    ),
    path(
        route="api/v1/comments/delete-comment",
        view=views.CommentDeleteAPIView.as_view(),
        name="api-v1-comments-delete-comment",
    ),
]
