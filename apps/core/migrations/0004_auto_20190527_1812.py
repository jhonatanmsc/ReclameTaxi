# Generated by Django 2.2.1 on 2019-05-27 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_driver_placa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='descr',
            field=models.TextField(blank=True, null=True),
        ),
    ]