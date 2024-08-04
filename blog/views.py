from django.shortcuts import render
from .models import Article, ArticleComment, ArticleTag, ArticleCategory


def blog(request):
    return render(
        request=request,
        template_name="blog/blog.html",
        context={
            "title": "Blog",
            "articles": Article.objects.all(),
            "article_categories": ArticleCategory.objects.all(),
            "article_tags": ArticleTag.objects.all(),
            "comments": ArticleComment.objects.all(),
        }
    )


def articles_by_category(request, category_slug):
    category = ArticleCategory.objects.get(slug=category_slug)

    return render(
        request=request,
        template_name="blog/articles-by-category.html",
        context={
            "title": category.name,
            "category": category,
            "articles": Article.objects.filter(article_category=category)
        }
    )


def articles_by_tag(request, tag_slug):
    tag = ArticleTag.objects.get(slug=tag_slug)

    return render(
        request=request,
        template_name="blog/articles-by-tag.html",
        context={
            "title": tag.name,
            "tag": tag,
            "articles": Article.objects.filter(article_tag=tag),
        }
    )


def article_details(request, category_slug, article_slug):
    category = ArticleCategory.objects.get(slug=category_slug)
    article = Article.objects.get(slug=article_slug, article_category=category)

    return render(
        request=request,
        template_name="blog/article-details.html",
        context={
            "title": article.title,
            "article": article,
            "category": category,
        }
    )
