from django.db import models
from datetime import datetime


# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name
