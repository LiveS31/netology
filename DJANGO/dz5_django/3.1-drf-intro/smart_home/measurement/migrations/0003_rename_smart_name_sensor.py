# Generated by Django 4.2 on 2023-05-31 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurements_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Smart_name',
            new_name='Sensor',
        ),
    ]