# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(blank=True, db_index=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
