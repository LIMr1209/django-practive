from django.db import models
from datetime import datetime


# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='学生姓名')
    age = models.IntegerField(default=18, verbose_name='学生年龄')
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, verbose_name='学生身高')
    stuid = models.CharField(max_length=10, unique=True, verbose_name='学生学号')
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), default='girls', max_length=10,
                              verbose_name='学生性别')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    # add_time = models.DateTimeField(auto_now_add=False,verbose_name='添加时间')
    def __str__(self):
        return self.name

    # add_time = models.DateTimeField(add_time=False, verbose_name='添加时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        db_table = 'student_info'
        ordering = ['name']
        verbose_name = '学生信息表'
        verbose_name_plural = verbose_name
