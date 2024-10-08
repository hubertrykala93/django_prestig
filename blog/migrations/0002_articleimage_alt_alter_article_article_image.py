# Generated by Django 5.1 on 2024-09-01 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="articleimage",
            name="alt",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="article_image",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="blog.articleimage",
            ),
        ),
    ]
