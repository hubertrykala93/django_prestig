# Generated by Django 5.0.6 on 2024-08-30 08:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0018_alter_article_description"),
    ]

    operations = [
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
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(null=True, upload_to="blog/article_images"),
                ),
                ("size", models.IntegerField(null=True)),
                ("width", models.IntegerField(null=True)),
                ("height", models.IntegerField(null=True)),
                ("format", models.CharField(null=True)),
            ],
            options={
                "verbose_name": "Article Image",
                "verbose_name_plural": "Article Images",
            },
        ),
    ]
