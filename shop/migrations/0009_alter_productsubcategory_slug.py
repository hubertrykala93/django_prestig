# Generated by Django 5.1 on 2024-09-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_alter_product_gallery"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productsubcategory",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]