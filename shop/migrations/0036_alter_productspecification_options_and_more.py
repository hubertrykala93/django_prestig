# Generated by Django 5.1 on 2024-09-13 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0035_remove_product_additional_information_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productspecification",
            options={
                "verbose_name": "Product Specification",
                "verbose_name_plural": "Product Specifications",
            },
        ),
        migrations.RemoveField(model_name="productspecification", name="hip",),
    ]