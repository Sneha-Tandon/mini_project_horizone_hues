# Generated by Django 4.2.3 on 2024-03-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HorizonHues', '0018_rename_iterary_image1_buy_now_itenary_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='group',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.CharField(default=None, max_length=2000, null=True),
        ),
    ]
