# Generated by Django 2.2.11 on 2020-03-21 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200321_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='seller',
            name='shop_category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
        ),
    ]
