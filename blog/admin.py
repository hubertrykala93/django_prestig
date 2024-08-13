from django.contrib import admin
from .models import ArticleCategory, ArticleTag, Article, ArticleComment
from .forms import ArticleCategoryForm, ArticleTagForm, ArticleForm, ArticleCommentForm


@admin.register(ArticleCategory)
class AdminArticleCategory(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    prepopulated_fields = {
        "slug": ["name"],
    }
    form = ArticleCategoryForm
    fieldsets = (
        (
            "Category Name", {
                "fields": [
                    "name",
                ],
            },
        ),
    )


@admin.register(ArticleTag)
class AdminArticleTag(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    prepopulated_fields = {
        "slug": ["name"],
    }
    form = ArticleTagForm
    fieldsets = (
        (
            "Tag Name", {
                "fields": [
                    "name",
                ],
            },
        ),
    )


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = [
        "id",
        "formatted_created_at",
        "user",
        "title",
        "slug",
        "description",
        "get_category",
        "article_tags"
    ]
    prepopulated_fields = {
        "slug": ["title"],
    }
    form = ArticleForm
    fieldsets = (
        (
            "Article Author", {
                "fields": [
                    "user",
                ],
            },
        ),
        (
            "Article Content", {
                "fields": [
                    "title",
                    "description",
                ],
            },
        ),
        (
            "Article Relations", {
                "fields": [
                    "article_category",
                    "article_tag",
                ],
            },
        ),
    )

    def get_category(self, obj):
        return obj.article_category.name

    get_category.short_description = "Category"

    def article_tags(self, obj):
        return "\n".join([t.name for t in obj.article_tag.all()])

    article_tags.short_description = "Tags"

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"


@admin.register(ArticleComment)
class AdminArticleComment(admin.ModelAdmin):
    list_display = [
        "id",
        "formatted_created_at",
        "user",
        "get_fullname",
        "email",
        "message",
        "is_active"
    ]
    form = ArticleCommentForm
    fieldsets = (
        (
            "Commented Article", {
                "fields": [
                    "article",
                ],
            },
        ),
        (
            "Commenter", {
                "fields": [
                    "user",
                    "fullname",
                    "email",
                ],
            },
        ),
        (
            "Comment Content", {
                "fields": [
                    "message",
                ],
            },
        ),
        (
            "Permissions", {
                "fields": [
                    "is_active",
                ],
            },
        ),
    )

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def get_fullname(self, obj):
        return obj.fullname

    get_fullname.short_description = "Full Name"
