# Generated by Django 2.2.11 on 2020-03-21 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200321_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latidude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.AlterField(
            model_name='driver',
            name='gps_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Location'),
        ),
    ]
