# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-15 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=16)),
                ('c_cost', models.IntegerField(default=18)),
            ],
        ),
    ]
