from django.contrib import admin
from .models import ArticleCategory, ArticleTag, Article, ArticleComment
from .forms import ArticleCategoryForm, ArticleTagForm, ArticleForm, ArticleCommentForm
from django_summernote.admin import SummernoteModelAdmin


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
class AdminArticle(SummernoteModelAdmin):
    summernote_fields = ["description"]
    list_display = [
        "id",
        "formatted_created_at",
        "user",
        "title",
        "get_image_name",
        "slug",
        "description",
        "get_category",
        "get_tags",
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
            "Uploading", {
                "fields": [
                    "image",
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
                    "article_tags",
                ],
            },
        ),
    )

    def get_image_name(self, obj):
        if obj.image:
            return obj.image.name.split("/")[-1]

    get_image_name.short_description = "Image"

    def get_category(self, obj):
        return obj.article_category.name

    get_category.short_description = "Category"

    def get_tags(self, obj):
        return "\n".join([t.name for t in obj.article_tags.all()])

    get_tags.short_description = "Tags"

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"


@admin.register(ArticleComment)
class AdminArticleComment(admin.ModelAdmin):
    list_display = [
        "id",
        "formatted_created_at",
        "article",
        "user",
        "get_fullname",
        "email",
        "comment",
        "is_active"
    ]
    list_editable = ["is_active"]
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
                    "comment",
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
