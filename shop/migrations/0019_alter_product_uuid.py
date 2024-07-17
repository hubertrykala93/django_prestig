# Generated by Django 5.0.6 on 2024-07-11 12:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0018_rename_product_category_product_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("422bb8a0-ce6c-40a6-ae35-73671b225467"), unique=True
            ),
        ),
    ]