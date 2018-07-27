# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-23 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_merge_20180621_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverify',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '修改'), ('change_email', '修改邮箱')], max_length=20, verbose_name='验证码类型'),
        ),
    ]
