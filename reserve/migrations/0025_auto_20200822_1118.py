# Generated by Django 3.1 on 2020-08-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0024_auto_20200822_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visittime',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='visittime',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
