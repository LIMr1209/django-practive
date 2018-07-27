from django.db import models
from datetime import datetime


# Create your models here.
class LoLHero(models.Model):
    name = models.CharField(max_length=20, verbose_name='英雄姓名')
    byname = models.CharField(max_length=20, verbose_name='英雄别名')
    price = models.IntegerField(verbose_name='英雄价格', null=True, blank=True)
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), default='boy', max_length=10, verbose_name='英雄性别')
    type = models.CharField(max_length=10, null=True, blank=True, verbose_name='英雄类型')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    def __str__(self):
        return self.name
    class Meta():
        db_table = 'LOLHero'
        ordering = ['name']
        verbose_name = '英雄资料表'
        verbose_name_plural = verbose_name
