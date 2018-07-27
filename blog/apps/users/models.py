from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name='用户昵称')

    def __str__(self):
        return self.username

    class Meta:
        # 自己创建的模型类需要继承时，指明abstract
        # abstract = True
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
