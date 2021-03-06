# Generated by Django 2.2.11 on 2020-03-21 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('province', models.TextField()),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=20)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('0', 'Sonstiges'), ('1', 'Lebensmittel'), ('2', 'Getränke'), ('3', 'Kleidung'), ('4', 'Schuhe'), ('5', 'Drogerie'), ('6', 'Optiker'), ('7', 'Haushaltswaren'), ('8', 'Elektronikwaren'), ('9', 'Outdoor & Sport'), ('10', 'Kunst & Musik'), ('11', 'Schreibwaren'), ('12', 'Geschenke'), ('13', 'Wäscherei'), ('14', 'Tabakwaren'), ('15', 'Spielzeugwaren')], default='0', max_length=2)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('A', 'Available'), ('U', 'Unavailable'), ('I', 'Idle')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latidude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=300)),
                ('phonenumber', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('O', 'Open'), ('C', 'Closed'), ('I', 'Idle')], max_length=1)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Address')),
                ('shop_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('loaded', models.DateTimeField(blank=True, null=True)),
                ('delivered', models.DateTimeField(blank=True, null=True)),
                ('transaction_content', models.CharField(max_length=600)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Buyer')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Driver')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='gps_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Location'),
        ),
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
