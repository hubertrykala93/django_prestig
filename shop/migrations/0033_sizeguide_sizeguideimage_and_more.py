# Generated by Django 5.1 on 2024-09-13 11:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0032_alter_productreview_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="SizeGuide",
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
                ("bust", models.CharField(max_length=10)),
                ("waist", models.CharField(max_length=10)),
                ("hip", models.CharField(max_length=10)),
                ("sleeve", models.CharField(max_length=10)),
            ],
            options={
                "verbose_name": "Size Guide",
                "verbose_name_plural": "Sizes Guides",
            },
        ),
        migrations.CreateModel(
            name="SizeGuideImage",
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
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="shop/size_guides")),
                ("size", models.IntegerField(null=True)),
                ("width", models.IntegerField(null=True)),
                ("height", models.IntegerField(null=True)),
                ("format", models.CharField(max_length=100, null=True)),
                ("alt", models.CharField(max_length=1000, null=True)),
            ],
            options={
                "verbose_name": "Size Guide Image",
                "verbose_name_plural": "Size Guide Images",
            },
        ),
        migrations.AddField(
            model_name="productsubcategory",
            name="size_guide",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.sizeguide",
            ),
        ),
        migrations.AddField(
            model_name="sizeguide",
            name="size_guide_image",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.sizeguideimage",
            ),
        ),
    ]