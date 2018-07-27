from django.contrib import admin
from .models import Category, ArticleInfo, TagInfo, ArticleTags, CommentInfo
import xadmin

# Register your models here.


class ArticleInfoAdmin(object):
    list_display = ['title', 'desc', 'content', 'author', 'image', 'category',
                    'click_num', 'love_num', 'comment_num', 'add_time']
    fields = ['title', 'desc', 'content', 'author', 'image', 'category',
              'click_num', 'love_num', 'comment_num', 'add_time']


class CategoryAdmin(object):
    list_display = ['name', 'add_time']
    fields = ['add_time', 'name']


class TagInfoAdmin(object):
    list_display = ['name', 'add_time']
    fields = ['add_time', 'name']


class ArticleTagsAdmin(object):
    list_display = ['article_info', 'tag_info', 'add_time']
    fields = ['article_info', 'tag_info', 'add_time']


class CommentInfoAdmin(object):
    list_display = ['comment_man', 'comment_article', 'comment_content', 'add_time']
    fields = ['comment_man', 'comment_article', 'comment_content', 'add_time']


xadmin.site.register(ArticleInfo, ArticleInfoAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(ArticleTags, ArticleTagsAdmin)
xadmin.site.register(TagInfo, TagInfoAdmin)
xadmin.site.register(CommentInfo, CommentInfoAdmin)
