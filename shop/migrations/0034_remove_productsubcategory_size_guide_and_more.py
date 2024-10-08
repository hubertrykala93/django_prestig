# Generated by Django 5.1 on 2024-09-13 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0033_sizeguide_sizeguideimage_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="productsubcategory", name="size_guide",),
        migrations.AddField(
            model_name="productsubcategory",
            name="size_guide_image",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.sizeguideimage",
            ),
        ),
        migrations.CreateModel(
            name="AdditionalInformation",
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
                ("chest", models.CharField(blank=True, max_length=10, null=True)),
                ("shoulder", models.CharField(blank=True, max_length=10, null=True)),
                ("waist", models.CharField(blank=True, max_length=10, null=True)),
                ("hip", models.CharField(blank=True, max_length=10, null=True)),
                ("sleeve", models.CharField(blank=True, max_length=10, null=True)),
                ("length", models.CharField(blank=True, max_length=10, null=True)),
                ("width", models.CharField(blank=True, max_length=10, null=True)),
                ("inches", models.CharField(blank=True, max_length=10, null=True)),
                ("knee", models.CharField(blank=True, max_length=10, null=True)),
                ("leg_opening", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "size_guide_image",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.sizeguideimage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Size Guide",
                "verbose_name_plural": "Sizes Guides",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="additional_information",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.additionalinformation",
            ),
        ),
        migrations.DeleteModel(name="SizeGuide",),
    ]
