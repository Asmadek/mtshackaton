# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-16 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_person_istate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]