# Generated by Django 5.0.6 on 2024-07-11 11:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0013_alter_product_uuid_alter_productgallery_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="brand", old_name="brand_description", new_name="description",
        ),
        migrations.RenameField(
            model_name="brand", old_name="brand_name", new_name="name",
        ),
        migrations.AlterField(
            model_name="product",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("06e4e3db-cf80-417d-a45c-01acf3537473"), unique=True
            ),
        ),
    ]
