# Generated by Django 3.1 on 2020-08-17 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0004_auto_20200817_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='uusername',
        ),
    ]
