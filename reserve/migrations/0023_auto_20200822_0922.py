# Generated by Django 3.1 on 2020-08-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0022_auto_20200822_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='doc1',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='doc2',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='user', max_length=10),
        ),
    ]
