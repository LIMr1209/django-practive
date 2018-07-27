# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-11 11:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180610_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('article_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleInfo', verbose_name='所属文章')),
            ],
            options={
                'verbose_name': '文章标签信息表',
                'verbose_name_plural': '文章标签信息表',
            },
        ),
        migrations.CreateModel(
            name='TagInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='标签名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '标签信息',
                'verbose_name_plural': '标签信息',
            },
        ),
        migrations.AddField(
            model_name='articletags',
            name='tag_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.TagInfo', verbose_name='所属标签'),
        ),
    ]
