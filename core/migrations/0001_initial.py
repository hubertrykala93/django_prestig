# Generated by Django 5.0.6 on 2024-07-25 13:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactMail",
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
                ("date_sent", models.DateTimeField(default=django.utils.timezone.now)),
                ("fullname", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=150)),
                ("subject", models.CharField(max_length=150)),
                ("message", models.TextField(max_length=2000)),
            ],
            options={
                "verbose_name": "Contact Mail",
                "verbose_name_plural": "Contact Mails",
            },
        ),
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
                ("email", models.EmailField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Newsletter",
                "verbose_name_plural": "Newsletters",
            },
        ),
    ]
