# Generated by Django 5.1 on 2024-09-01 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_alter_product_sku"),
    ]

    operations = [
        migrations.AddField(
            model_name="brandlogo",
            name="alt",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name="productcategoryimage",
            name="alt",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name="productimage",
            name="alt",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name="productsubcategoryimage",
            name="alt",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="brand",
            name="logo",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="shop.brandlogo",
            ),
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="category_image",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="shop.productcategoryimage",
            ),
        ),
        migrations.AlterField(
            model_name="productsubcategory",
            name="subcategory_image",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="shop.productsubcategoryimage",
            ),
        ),
    ]