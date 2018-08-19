# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-19 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, verbose_name='购买数量')),
                ('is_select', models.BooleanField(default=True, verbose_name='是否选中')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='所属商品')),
            ],
            options={
                'verbose_name': '购物车信息',
                'verbose_name_plural': '购物车信息',
            },
        ),
    ]
