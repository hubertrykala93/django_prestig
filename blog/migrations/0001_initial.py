# Generated by Django 5.1 on 2024-08-31 13:14

import accounts.mixins
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticleCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Article Category",
                "verbose_name_plural": "Article Categories",
            },
        ),
        migrations.CreateModel(
            name="ArticleImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(null=True, upload_to="blog/article_images"),
                ),
                ("size", models.IntegerField(null=True)),
                ("width", models.IntegerField(null=True)),
                ("height", models.IntegerField(null=True)),
                ("format", models.CharField(max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Article Image",
                "verbose_name_plural": "Article Images",
            },
            bases=(accounts.mixins.SaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name="ArticleTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Article Tag",
                "verbose_name_plural": "Article Tags",
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=500, unique=True)),
                ("description", models.TextField(max_length=100000)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "article_category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blog.articlecategory",
                    ),
                ),
                (
                    "article_image",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.articleimage",
                    ),
                ),
                ("article_tags", models.ManyToManyField(to="blog.articletag")),
            ],
            options={"verbose_name": "Article", "verbose_name_plural": "Articles",},
        ),
        migrations.CreateModel(
            name="ArticleComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("fullname", models.CharField(blank=True, max_length=100)),
                ("email", models.EmailField(blank=True, max_length=100)),
                ("comment", models.TextField(max_length=20000)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.article",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": "Comment", "verbose_name_plural": "Comments",},
        ),
    ]
