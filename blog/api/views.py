from rest_framework.generics import DestroyAPIView, CreateAPIView
from blog.models import ArticleComment, Article
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
import urllib.parse


class CommentCreateAPIView(CreateAPIView):
    def get_serializer_class(self):
        return CommentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            article = Article.objects.get(slug=request.data.get("slug"))

        except Article.DoesNotExist:
            return Response(
                data={
                    "error": "The article you want to comment on does not exist.",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(article=Article.objects.get(slug="the-influence-of-minimalism-on-contemporary-fashion"),
                                user=request.user, email=request.user.email)

            else:
                serializer.save(article=Article.objects.get(slug="the-influence-of-minimalism-on-contemporary-fashion"))

            response = Response(
                data={
                    "success": "Your comment must be approved by the administrator.",
                },
                status=status.HTTP_201_CREATED,
            )

            if request.data.get("save") == "1":
                response.set_cookie(
                    key="fullname",
                    value=urllib.parse.quote(string=request.data.get("fullname")),
                    max_age=60 * 60 * 24 * 365
                )
                response.set_cookie(
                    key="email",
                    value=urllib.parse.quote(string=request.data.get("email")),
                    max_age=60 * 60 * 24 * 365
                )

            return response

        else:
            return Response(
                data=serializer.errors,
            )


class CommentDeleteAPIView(DestroyAPIView):
    def get_object(self):
        try:
            comment_id = int(self.request.data.get("commentid"))

            return ArticleComment.objects.get(id=comment_id, user=self.request.user)

        except (ArticleComment.DoesNotExist, ValueError):
            return None

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance is None:
            return Response(
                data={
                    "error": "An error occurred while trying to delete comment.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        temp_id = instance.id
        article = ArticleComment.objects.get(id=instance.id).article

        instance.delete()

        comments = ArticleComment.objects.filter(article=article, is_active=True).order_by("-created_at")

        return Response(
            data={
                "success": "Your comment has been successfully deleted.",
                "id": temp_id,
                "total": len(comments),
            },
            status=status.HTTP_200_OK,
        )
