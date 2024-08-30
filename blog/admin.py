from django.contrib import admin
from .models import ArticleCategory, ArticleTag, Article, ArticleComment, ArticleImage
from .forms import ArticleCategoryForm, ArticleTagForm, ArticleForm, ArticleCommentForm, ArticleImageForm
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


@admin.register(ArticleImage)
class AdminArticleImage(admin.ModelAdmin):
    """
    Admin options and functionalities for ArticleImage model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "formatted_updated_at",
        "image",
        "formatted_image_name",
        "size",
        "width",
        "height",
    ]
    form = ArticleImageForm
    fieldsets = (
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
    )

    def formatted_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def formatted_updated_at(self, obj):
        if obj.updated_at:
            return obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")

        return "No Updated Yet"

    formatted_updated_at.description = "Updated At"

    def formatted_image_name(self, obj):
        if obj.image:
            return obj.image.name.split("/")[-1]

        return "No Article Image"

    formatted_image_name.short_description = "Article Image Name"


@admin.register(Article)
class AdminArticle(SummernoteModelAdmin):
    summernote_fields = ["description"]
    list_display = [
        "id",
        "formatted_created_at",
        "get_user_id",
        "user",
        "title",
        "get_image",
        "get_image_name",
        "slug",
        "get_category_id",
        "get_category_name",
        "get_tag_ids",
        "get_tag_names",
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
                    "article_image",
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

    def get_user_id(self, obj):
        return obj.user.id

    get_user_id.short_description = "User ID"

    def get_image(self, obj):
        if obj.article_image:
            return obj.article_image

    get_image.short_description = "Image ID"

    def get_image_name(self, obj):
        if obj.article_image:
            return obj.article_image.image.name.split(sep="/")[-1]

    get_image_name.short_description = "Image"

    def get_category_id(self, obj):
        return obj.article_category.id

    get_category_id.short_description = "Category ID"

    def get_category_name(self, obj):
        return obj.article_category.name

    get_category_name.short_description = "Category"

    def get_tag_ids(self, obj):
        from django.utils.html import format_html_join
        from django.utils.safestring import mark_safe
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((tag.id,) for tag in obj.article_tags.all())
        ) or mark_safe("-")

    get_tag_ids.short_description = "Tag ID"

    def get_tag_names(self, obj):
        from django.utils.html import format_html_join
        from django.utils.safestring import mark_safe
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((tag.name,) for tag in obj.article_tags.all())
        ) or mark_safe("-")

    get_tag_names.short_description = "Tag"

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"


@admin.register(ArticleComment)
class AdminArticleComment(admin.ModelAdmin):
    list_display = [
        "id",
        "formatted_created_at",
        "get_user_id",
        "user",
        "get_article_id",
        "article",
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

    def get_user_id(self, obj):
        return obj.user.id

    get_user_id.short_description = "User ID"

    def get_article_id(self, obj):
        return str(obj.article.id)

    get_article_id.short_description = "Article ID"

    def get_fullname(self, obj):
        return obj.fullname

    get_fullname.short_description = "Full Name"
