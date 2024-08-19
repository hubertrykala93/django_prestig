from blog.models import Article, ArticleTag, ArticleCategory
from django.db.models import Count


def blog_sidebar(request):
    return {
        "categories_with_counts": ArticleCategory.objects.annotate(num_articles=Count("article")).distinct(),
        "article_tags": ArticleTag.objects.all().order_by("name"),
        "latest_articles": Article.objects.filter().order_by("-created_at")[:3],
    }
