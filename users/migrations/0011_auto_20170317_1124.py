# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-17 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20170317_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areaanswer',
            name='AreaQuestion',
        ),
        migrations.RemoveField(
            model_name='areaquestion',
            name='area',
        ),
        migrations.AddField(
            model_name='person',
            name='attr',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.DeleteModel(
            name='AreaAnswer',
        ),
        migrations.DeleteModel(
            name='AreaQuestion',
        ),
    ]
