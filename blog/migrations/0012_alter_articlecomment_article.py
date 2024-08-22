# Generated by Django 5.0.6 on 2024-08-22 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlecomment",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog.article",
            ),
        ),
    ]
