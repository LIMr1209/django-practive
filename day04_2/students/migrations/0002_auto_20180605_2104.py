# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-05 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardid',
            options={'verbose_name': '学号信息表', 'verbose_name_plural': '学号信息表'},
        ),
    ]