# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-28 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_is_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifycode',
            name='send_type',
            field=models.CharField(choices=[('register', '注册激活'), ('forget', '重置密码'), ('change', '修改邮箱')], max_length=15, verbose_name='发送类别'),
        ),
    ]
