# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-29 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newres', '0003_auto_20190129_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='group',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
