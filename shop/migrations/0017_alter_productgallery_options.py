# Generated by Django 5.0.6 on 2024-08-30 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0016_alter_productgallery_options_rename_size_size_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productgallery",
            options={
                "verbose_name": "Product Gallery",
                "verbose_name_plural": "Products Gallery",
            },
        ),
    ]
