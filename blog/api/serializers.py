from blog.models import ArticleComment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = "__all__"
