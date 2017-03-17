# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-16 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170316_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.City'),
        ),
        migrations.AlterField(
            model_name='person',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.University'),
        ),
    ]
