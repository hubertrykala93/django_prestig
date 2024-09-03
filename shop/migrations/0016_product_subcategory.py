# Generated by Django 5.1 on 2024-09-03 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0015_alter_productsubcategory_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.productsubcategory",
            ),
        ),
    ]
