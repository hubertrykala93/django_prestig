# Generated by Django 5.0.6 on 2024-08-19 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_article_slug_alter_articlecategory_slug_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article", old_name="article_tag", new_name="article_tags",
        ),
    ]
