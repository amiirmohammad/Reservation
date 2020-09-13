# Generated by Django 3.1 on 2020-08-22 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0028_auto_20200822_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visittime',
            name='doctor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='reserve.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visittime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='reserve.user'),
        ),
    ]
