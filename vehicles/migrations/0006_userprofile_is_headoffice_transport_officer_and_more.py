# Generated by Django 5.0.3 on 2024-04-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_rename_name_fueltype_fuel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_HeadOffice_Transport_Officer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_Provincial_Transport_Officer',
            field=models.BooleanField(default=False),
        ),
    ]