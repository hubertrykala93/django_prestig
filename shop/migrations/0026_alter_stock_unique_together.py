# Generated by Django 5.1 on 2024-09-04 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0025_remove_product_quantity_stock_product"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="stock", unique_together={("product", "color", "size")},
        ),
    ]
