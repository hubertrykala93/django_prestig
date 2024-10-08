# Generated by Django 5.1 on 2024-09-04 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0028_productreview_rate_delete_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productsubcategory",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_subcategories",
                to="shop.productcategory",
            ),
        ),
    ]
