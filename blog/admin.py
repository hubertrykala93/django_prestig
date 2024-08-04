from django.contrib import admin
from .models import ArticleCategory, ArticleTag, Article, ArticleComment
from .forms import ArticleCategoryForm, ArticleTagForm, ArticleForm, ArticleCommentForm


@admin.register(ArticleCategory)
class AdminArticleCategory(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["id", "name", "slug"]
    prepopulated_fields = {
        "slug": ["name"],
    }
    form = ArticleCategoryForm


@admin.register(ArticleTag)
class AdminArticleTag(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["id", "name", "slug"]
    prepopulated_fields = {
        "slug": ["name"],
    }
    form = ArticleTagForm


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    fields = ["user", "title", "description", "article_category", "article_tag"]
    list_display = ["id", "created_at", "user", "title", "slug", "description", "article_category", "article_tags"]
    prepopulated_fields = {
        "slug": ["title"],
    }
    form = ArticleForm

    def article_tags(self, obj):
        return "\n".join([t.name for t in obj.article_tag.all()])


@admin.register(ArticleComment)
class AdminArticleComment(admin.ModelAdmin):
    fields = ["article", "user", "fullname", "email", "message", "is_active"]
    list_display = ["id", "created_at", "user", "fullname", "email", "message", "is_active"]
    form = ArticleCommentForm
