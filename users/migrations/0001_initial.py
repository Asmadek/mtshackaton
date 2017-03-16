# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-16 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('is_right', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date_birth', models.DateField()),
                ('vk', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=15)),
                ('chat_id', models.CharField(max_length=128)),
                ('telegram_id', models.CharField(max_length=128)),
                ('photo_url', models.CharField(max_length=128)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.City')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Area')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('has_internship', models.BooleanField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Area')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Test'),
        ),
        migrations.AddField(
            model_name='person',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.University'),
        ),
        migrations.AddField(
            model_name='answer',
            name='queistion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Question'),
        ),
    ]
