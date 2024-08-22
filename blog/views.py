from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article, ArticleCategory, ArticleComment, ArticleTag
from django.db.models import Q


def blog(request):
    return render(
        request=request,
        template_name="blog/blog.html",
        context={
            "title": "Blog",
            "articles": Article.objects.all().order_by("-created_at"),
        }
    )


def articles_by_category(request, category_slug):
    try:
        category = ArticleCategory.objects.get(slug=category_slug)

    except ArticleCategory.DoesNotExist:
        messages.info(
            request=request,
            message=f"The article category named '{category_slug.replace('-', ' ').title()}' does not exist."
        )

        return redirect(to="blog")

    return render(
        request=request,
        template_name="blog/articles-by-category.html",
        context={
            "title": category.name,
            "articles": Article.objects.filter(article_category=category).order_by("-created_at"),
        }
    )


def articles_by_tag(request, tag_slug):
    try:
        tag = ArticleTag.objects.get(slug=tag_slug)

    except ArticleTag.DoesNotExist:
        messages.info(
            request=request,
            message=f"The tag named '{tag_slug.replace('-', ' ').title()}' does not exist."
        )
        return redirect(to="blog")

    return render(
        request=request,
        template_name="blog/articles-by-tag.html",
        context={
            "title": tag.name,
            "articles": Article.objects.filter(article_tags=tag).order_by("-created_at"),
        }
    )


def article_details(request, category_slug, article_slug):
    category = ArticleCategory.objects.get(slug=category_slug)
    article = Article.objects.get(slug=article_slug, article_category=category)
    comments = ArticleComment.objects.filter(article=article, is_active=True).order_by("-created_at")

    return render(
        request=request,
        template_name="blog/article-details.html",
        context={
            "title": article.title,
            "article": article,
            "comments": comments,
            "total_comments": len(comments),
        }
    )


def search_by_keyword(request):
    articles = []
    keyword = request.GET.get("keyword", None)

    if keyword:
        words = keyword.split()
        query = Q()

        for word in words:
            q = Q(title__icontains=word) | Q(description__icontains=word)
            query |= q

        articles = Article.objects.filter(query).order_by("-created_at")

    if not articles:
        messages.error(
            request=request,
            message=f"No articles found matching your search criteria.",
        )

    return render(
        request=request,
        template_name="blog/blog.html",
        context={
            "title": "Search Results",
            "articles": articles,
        }
    )
