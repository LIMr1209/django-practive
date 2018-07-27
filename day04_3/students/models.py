from django.db import models
from datetime import datetime


# Create your models here.
class BanClass(models.Model):
    name = models.CharField(max_length=10, verbose_name='班级名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='开班时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级信息表'
        verbose_name_plural = verbose_name


class StudentsInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='学生姓名')
    age = models.IntegerField(default=18, verbose_name='学生年龄')
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), default='girl', max_length=10, verbose_name='学生性别')
    stu_class = models.ForeignKey(BanClass, verbose_name='所属班级')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生信息表'
        verbose_name_plural = verbose_name


class CardId(models.Model):
    id_number = models.CharField(max_length=10, verbose_name='学生学号')
    student = models.OneToOneField(StudentsInfo, verbose_name='所属学生')

    def __str__(self):
        return self.id_number

    class Meta:
        verbose_name = '学号信息表'
        verbose_name_plural = verbose_name
