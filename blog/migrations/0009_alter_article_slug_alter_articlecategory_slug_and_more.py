# Generated by Django 5.0.6 on 2024-08-10 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_article_article_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name="articlecategory",
            name="slug",
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name="articletag", name="slug", field=models.SlugField(unique=True),
        ),
    ]