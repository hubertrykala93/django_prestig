# Generated by Django 5.0.6 on 2024-08-23 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_alter_articlecomment_article"),
    ]

    operations = [
        migrations.RenameField(
            model_name="articlecomment", old_name="message", new_name="comment",
        ),
    ]
