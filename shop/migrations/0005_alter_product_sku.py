# Generated by Django 5.1 on 2024-09-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_alter_product_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="sku",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
