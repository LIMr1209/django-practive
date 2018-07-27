from django.db import models
from datetime import datetime
from users.models import UserProfile


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name='文章类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别信息'
        verbose_name_plural = verbose_name


class ArticleInfo(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=100, verbose_name='文章简介')
    content = models.TextField(verbose_name='文章内容')
    click_num = models.IntegerField(default=0, verbose_name='文章点击量')
    love_num = models.IntegerField(default=0, verbose_name='文章点赞量')
    comment_num = models.IntegerField(default=0, verbose_name='文章评论数')
    image = models.ImageField(upload_to='article/%y/%m/%d', max_length=200, verbose_name='文章封面图')
    author = models.ForeignKey(UserProfile, verbose_name='所属作者')
    category = models.ForeignKey(Category, verbose_name='所属类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发表时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = verbose_name


class TagInfo(models.Model):
    name = models.CharField(max_length=10, verbose_name='标签名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签信息'
        verbose_name_plural = verbose_name


class ArticleTags(models.Model):
    article_info = models.ForeignKey(ArticleInfo, verbose_name='所属文章')
    tag_info = models.ForeignKey(TagInfo, verbose_name='所属标签')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.article_info.title

    class Meta:
        verbose_name = '文章标签信息表'
        verbose_name_plural = verbose_name


class CommentInfo(models.Model):
    comment_man = models.ForeignKey(UserProfile,verbose_name='所属用户')
    comment_article = models.ForeignKey(ArticleInfo,verbose_name='所属文章')
    comment_content = models.CharField(max_length=200,verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.comment_man.username

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name

