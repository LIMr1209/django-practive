# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-25 11:15
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0006_merge_20180621_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orginfo',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='机构详情'),
        ),
    ]
