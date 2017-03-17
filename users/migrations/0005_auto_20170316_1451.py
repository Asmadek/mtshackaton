# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-16 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170316_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='category',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='chat_id',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
