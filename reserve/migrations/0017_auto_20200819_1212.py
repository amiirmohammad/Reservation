# Generated by Django 3.1 on 2020-08-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0016_auto_20200819_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='case_number',
            field=models.TextField(max_length=12),
        ),
    ]
