# Generated by Django 4.2.3 on 2024-03-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HorizonHues', '0012_package_days_package_nights'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycart',
            name='days',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='mycart',
            name='nights',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
