# Generated by Django 2.2.6 on 2019-10-20 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20191020_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 19, 28, 10, 474707)),
        ),
    ]