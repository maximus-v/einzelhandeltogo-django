# Generated by Django 2.2.11 on 2020-03-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200321_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='shop_image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
