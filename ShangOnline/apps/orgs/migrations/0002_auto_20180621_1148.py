# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-21 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orginfo',
            name='category',
            field=models.CharField(blank=True, choices=[('jg', '机构'), ('gx', '高校'), ('gr', '个人')], max_length=5, null=True, verbose_name='机构类别'),
        ),
        migrations.AddField(
            model_name='orginfo',
            name='course_num',
            field=models.IntegerField(default=0, verbose_name='课程数量'),
        ),
    ]
