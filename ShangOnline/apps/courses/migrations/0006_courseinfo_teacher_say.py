# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-21 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_courseinfo_need_know'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfo',
            name='teacher_say',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='老师告知'),
        ),
    ]
