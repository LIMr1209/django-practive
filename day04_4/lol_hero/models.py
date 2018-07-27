from django.db import models
from datetime import datetime


# Create your models here.

class Camp(models.Model):
    name = models.CharField(max_length=20, verbose_name='阵营名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '阵营信息表'
        verbose_name_plural = verbose_name


class Hero(models.Model):
    name = models.CharField(max_length=20, verbose_name='英雄姓名')
    byname = models.CharField(max_length=30, verbose_name='英雄别名')
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), default='boy', max_length=10, verbose_name='英雄性别')
    hero_camp = models.ForeignKey(Camp, verbose_name='所属阵营')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '英雄信息表'
        verbose_name_plural = verbose_name


class EnglishName(models.Model):
    name = models.CharField(max_length=20, verbose_name='英文名')
    hero = models.OneToOneField(Hero, verbose_name='所属英雄')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '英文名信息表'
        verbose_name_plural = verbose_name


