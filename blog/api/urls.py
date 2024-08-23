from django.urls import path
from . import views

urlpatterns = [
    path(
        route="api/v1/comments/delete-comment",
        view=views.CommentDeleteAPIView.as_view(),
        name="api-v1-comment-delete-comment",
    ),
]
