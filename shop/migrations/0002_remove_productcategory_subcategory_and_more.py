# Generated by Django 5.0.6 on 2024-07-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="productcategory", name="subcategory",),
        migrations.AddField(
            model_name="productcategory",
            name="subcategory",
            field=models.ManyToManyField(to="shop.productsubcategory"),
        ),
    ]
