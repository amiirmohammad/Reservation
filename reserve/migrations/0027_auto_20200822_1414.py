# Generated by Django 3.1 on 2020-08-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0026_auto_20200822_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visittime',
            name='empty',
            field=models.CharField(default='False', max_length=20),
        ),
    ]
