# Generated by Django 3.1 on 2020-08-22 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0029_auto_20200822_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visittime',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='visittime',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vtd',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='vtd',
            name='visit_time',
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='VisitTime',
        ),
        migrations.DeleteModel(
            name='VTD',
        ),
    ]