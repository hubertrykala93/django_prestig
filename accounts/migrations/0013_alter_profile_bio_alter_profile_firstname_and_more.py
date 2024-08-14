# Generated by Django 5.0.6 on 2024-08-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0012_rename_date_of_birth_profile_dateofbirth_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile", name="bio", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="profile",
            name="firstname",
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name="profile",
            name="gender",
            field=models.CharField(
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Undefined", "Undefined"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="lastname",
            field=models.CharField(max_length=35),
        ),
    ]