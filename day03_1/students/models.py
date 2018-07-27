from django.db import models
from datetime import datetime


# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='学生姓名')
    age = models.IntegerField(default=18, verbose_name='学生年龄')
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), verbose_name='学生性别', max_length=10, default='girl')
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, verbose_name='学生身高')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'students_info'
        ordering = ['height']
        verbose_name = '学生信息表'
        verbose_name_plural = verbose_name
