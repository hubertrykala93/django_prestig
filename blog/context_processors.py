from django.db.models import Count
from .models import Article, ArticleTag, ArticleCategory


def blog_sidebar(request):
    return {
        "article_counts": ArticleCategory.objects.annotate(num_articles=Count("article")).order_by("name"),
        "article_tags": ArticleTag.objects.all().order_by("name"),
        "latest_articles": Article.objects.all().order_by("-created_at")[:3],
    }
