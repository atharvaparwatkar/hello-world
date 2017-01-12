# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-10 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='student',
            field=models.ManyToManyField(blank=True, to='dashboard.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id_no',
            field=models.IntegerField(),
        ),
    ]
