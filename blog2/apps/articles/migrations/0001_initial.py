# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-11 19:31
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=200, verbose_name='文章简介')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('comment_num', models.IntegerField(default=0, verbose_name='评论数')),
                ('love_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('image', models.ImageField(max_length=200, upload_to='article/%y/%m/%d', verbose_name='文章封面')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属作者')),
            ],
            options={
                'verbose_name': '文章信息',
                'verbose_name_plural': '文章信息',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类别名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '类别信息',
                'verbose_name_plural': '类别信息',
            },
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Category', verbose_name='所属类别'),
        ),
    ]
