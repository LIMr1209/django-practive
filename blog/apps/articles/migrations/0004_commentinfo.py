# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-11 16:55
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_auto_20180611_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=200, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleInfo', verbose_name='所属文章')),
                ('comment_man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '评论信息',
                'verbose_name_plural': '评论信息',
            },
        ),
    ]
