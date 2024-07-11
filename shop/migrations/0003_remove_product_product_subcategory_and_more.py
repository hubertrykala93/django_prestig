# Generated by Django 5.0.6 on 2024-07-11 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_alter_product_sku"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="product_subcategory",),
        migrations.AddField(
            model_name="productcategory",
            name="subcategory",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.productsubcategory",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="sku",
            field=models.IntegerField(default=324454, unique=True),
        ),
    ]
