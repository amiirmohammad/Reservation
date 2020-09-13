# Generated by Django 3.1 on 2020-08-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=35)),
                ('password', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('verify', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
    ]