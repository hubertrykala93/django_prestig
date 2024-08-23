from rest_framework.generics import DestroyAPIView, CreateAPIView
from blog.models import ArticleComment, Article
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer


class CommentCreateAPIView(CreateAPIView):
    def get_serializer_class(self):
        return CommentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(article=Article.objects.get(slug="the-influence-of-minimalism-on-contemporary-fashion"),
                                user=request.user, email=request.user.email)

            else:
                serializer.save(article=Article.objects.get(slug="the-influence-of-minimalism-on-contemporary-fashion"))

            return Response(
                data={
                    "success": "Your comment must be approved by the administrator.",
                },
                status=status.HTTP_201_CREATED,
            )

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
                "summary": len(comments),
            },
            status=status.HTTP_200_OK,
        )
