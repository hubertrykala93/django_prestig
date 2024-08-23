from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article, ArticleCategory, ArticleComment, ArticleTag
from django.db.models import Q
from django.core.paginator import Paginator


def pagination(request, object_list, per_page=6):
    paginator = Paginator(object_list=object_list, per_page=per_page)
    page = request.GET.get("page")

    try:
        page = int(page)

        if page < 1:
            page = 1

        elif page > paginator.num_pages:
            page = paginator.num_pages

    except (TypeError, ValueError):
        page = 1

    pages = paginator.get_page(number=page)

    return pages


def blog(request):
    return render(
        request=request,
        template_name="blog/blog.html",
        context={
            "title": "Blog",
            "pages": pagination(
                request=request,
                object_list=Article.objects.all().order_by("-created_at"),
                per_page=6,
            ),
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
            "pages": pagination(
                request=request,
                object_list=Article.objects.filter(article_category=category).order_by("-created_at"),
                per_page=6,
            ),
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
            "pages": pagination(
                request=request,
                object_list=Article.objects.filter(article_tags=tag).order_by("-created_at"),
                per_page=6,
            ),
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
    print(request.GET.urlencode)
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
            "pages": pagination(
                request=request,
                object_list=articles,
                per_page=6,
            ),
        }
    )
