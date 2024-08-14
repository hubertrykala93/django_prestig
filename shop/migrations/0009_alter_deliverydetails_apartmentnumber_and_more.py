# Generated by Django 5.0.6 on 2024-08-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_alter_deliverydetails_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deliverydetails",
            name="apartmentnumber",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="deliverydetails",
            name="city",
            field=models.CharField(max_length=169),
        ),
        migrations.AlterField(
            model_name="deliverydetails",
            name="country",
            field=models.CharField(max_length=56),
        ),
        migrations.AlterField(
            model_name="deliverydetails",
            name="housenumber",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="deliverydetails",
            name="phone",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="deliverydetails",
            name="postalcode",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="deliverydetails",
            name="state",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="deliverydetails",
            name="street",
            field=models.CharField(max_length=50),
        ),
    ]