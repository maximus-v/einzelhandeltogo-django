# Generated by Django 2.2.11 on 2020-03-21 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200321_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='gps_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Location'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='gps_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Location'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='shop_category',
            field=models.CharField(choices=[('0', 'Sonstiges'), ('1', 'Lebensmittel'), ('2', 'Getränke'), ('3', 'Kleidung'), ('4', 'Schuhe'), ('5', 'Drogerie'), ('6', 'Optiker'), ('7', 'Haushaltswaren'), ('8', 'Elektronikwaren'), ('9', 'Outdoor & Sport'), ('10', 'Kunst & Musik'), ('11', 'Bücher & Schreibwaren'), ('12', 'Geschenke'), ('13', 'Wäscherei'), ('14', 'Tabakwaren'), ('15', 'Spielzeugwaren')], default='0', max_length=2),
        ),
    ]
