# Generated by Django 4.2 on 2023-05-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wearpon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.IntegerField()),
                ('rerety', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
