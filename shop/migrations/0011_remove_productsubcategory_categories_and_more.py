# Generated by Django 5.1 on 2024-09-02 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0010_alter_productsubcategory_slug"),
    ]

    operations = [
        migrations.RemoveField(model_name="productsubcategory", name="categories",),
        migrations.AddField(
            model_name="productsubcategory",
            name="categories",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.productcategory",
            ),
        ),
    ]
