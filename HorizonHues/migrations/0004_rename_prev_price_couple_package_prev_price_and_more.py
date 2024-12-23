# Generated by Django 4.2.3 on 2024-03-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HorizonHues', '0003_alter_package_discount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='prev_price_couple',
            new_name='prev_price',
        ),
        migrations.RemoveField(
            model_name='package',
            name='prev_price_family',
        ),
        migrations.RemoveField(
            model_name='package',
            name='prev_price_friends',
        ),
        migrations.AddField(
            model_name='package',
            name='group',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
