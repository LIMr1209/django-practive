# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-29 00:48
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courseinfo_is_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情'),
        ),
    ]
