# Generated by Django 4.2 on 2023-05-30 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurements',
            options={'ordering': ('created_at',)},
        ),
    ]
