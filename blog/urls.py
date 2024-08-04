from django.urls import path
from . import views as blog_views

urlpatterns = [
    path(route="blog", view=blog_views.blog, name="blog"),
    path(route="blog/category/<slug:category_slug>", view=blog_views.articles_by_category, name="articles-by-category"),
    path(route="blog/tag/<slug:tag_slug>", view=blog_views.articles_by_tag, name="articles-by-tag"),
    path(route="blog/<slug:category_slug>/<slug:article_slug>", view=blog_views.article_details,
         name="article-details"),
]
