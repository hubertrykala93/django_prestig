# Generated by Django 5.0.6 on 2024-08-04 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_profile_options_profile_website"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile", old_name="profile_picture", new_name="image",
        ),
    ]
