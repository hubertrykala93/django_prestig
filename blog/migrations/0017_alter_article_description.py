# Generated by Django 5.0.6 on 2024-08-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0016_alter_article_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="description",
            field=models.TextField(max_length=100000),
        ),
    ]
