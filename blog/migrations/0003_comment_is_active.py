# Generated by Django 5.0.6 on 2024-08-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_article_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
