# Generated by Django 5.0.6 on 2024-08-11 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_alter_deliverydetails_apartment_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productsubcategory",
            options={
                "verbose_name": "Product SubCategory",
                "verbose_name_plural": "Product SubCategories",
            },
        ),
    ]