# Generated by Django 2.2.11 on 2020-03-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_seller_shop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.TextField(blank=True, null=True),
        ),
    ]
