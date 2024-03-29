# Generated by Django 4.2 on 2023-06-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_alter_sensor_options_alter_sensor_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Температура'),
        ),
    ]
