# Generated by Django 5.0.6 on 2024-07-25 13:52

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=1000, unique=True)),
                ("description", models.CharField(max_length=10000)),
                ("logo", models.ImageField(upload_to="shop/brands")),
                ("slug", models.SlugField(unique=True)),
            ],
            options={"verbose_name": "Brand", "verbose_name_plural": "Brands",},
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", models.CharField(max_length=100)),
                ("hex", models.CharField(max_length=100, null=True)),
            ],
            options={"verbose_name": "Color", "verbose_name_plural": "Colors",},
        ),
        migrations.CreateModel(
            name="ProductGallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(null=True, upload_to="shop/products/gallery"),
                ),
            ],
            options={
                "verbose_name": "Product Gallery",
                "verbose_name_plural": "Products Gallery",
            },
        ),
        migrations.CreateModel(
            name="ProductSubCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField()),
                ("image", models.ImageField(upload_to="shop/subcategories")),
            ],
            options={
                "verbose_name": "Product Subcategory",
                "verbose_name_plural": "Product Subcategories",
            },
        ),
        migrations.CreateModel(
            name="ProductTags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Product Tag",
                "verbose_name_plural": "Product Tags",
            },
        ),
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("size", models.CharField(max_length=100)),
            ],
            options={"verbose_name": "Size", "verbose_name_plural": "Sizes",},
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(unique=True)),
                ("image", models.ImageField(upload_to="shop/categories")),
                ("is_active", models.BooleanField(default=True)),
                ("subcategory", models.ManyToManyField(to="shop.productsubcategory")),
            ],
            options={
                "verbose_name": "Product Category",
                "verbose_name_plural": "Product Categories",
            },
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.color"
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.size"
                    ),
                ),
            ],
            options={"verbose_name": "Stock", "verbose_name_plural": "Stocks",},
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("name", models.CharField(max_length=1000, unique=True)),
                ("slug", models.SlugField(unique=True)),
                ("short_description", models.CharField(max_length=10000)),
                ("price", models.FloatField()),
                ("thumbnail", models.ImageField(upload_to="shop/products/thumbnails")),
                ("rate", models.IntegerField()),
                ("full_description", models.TextField(max_length=100000)),
                ("sku", models.IntegerField(default=0, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_featured", models.BooleanField(default=False)),
                ("sales_counter", models.IntegerField(default=0)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.brand"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.productcategory",
                    ),
                ),
                ("gallery", models.ManyToManyField(to="shop.productgallery")),
                ("tags", models.ManyToManyField(to="shop.producttags")),
                ("quantity", models.ManyToManyField(to="shop.stock")),
            ],
            options={"verbose_name": "Product", "verbose_name_plural": "Products",},
        ),
    ]
