# Generated by Django 5.0.6 on 2024-07-11 14:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Newsletter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("email", models.EmailField(max_length=100)),
            ],
            options={
                "verbose_name": "Newsletter",
                "verbose_name_plural": "Newsletters",
            },
        ),
    ]
