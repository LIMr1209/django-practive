# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-13 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoinfo',
            name='lessoninfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.LessonInfo', verbose_name='所属章节'),
        ),
    ]
