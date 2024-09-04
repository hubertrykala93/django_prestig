# Generated by Django 5.1 on 2024-08-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_productimage_remove_product_gallery_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="gallery",),
        migrations.AddField(
            model_name="product",
            name="gallery",
            field=models.ManyToManyField(blank=True, to="shop.productimage"),
        ),
    ]