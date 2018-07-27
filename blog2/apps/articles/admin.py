from django.contrib import admin
from .models import ArticleInfo, Category, TagInfo, CommentInfo, ArticleTag


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_time']
    fields = ['name', 'add_time']


class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'content', 'click_num', 'comment_num', 'love_num', 'image', 'author', 'category',
                    'add_time']
    fields = ['title', 'desc', 'content', 'click_num', 'comment_num', 'love_num', 'image', 'author', 'category',
              'add_time']


class TagInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_time']
    fields = ['name', 'add_time']


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['articleinfo', 'add_time', 'taginfo']
    fields = ['articleinfo', 'add_time', 'taginfo']


class CommentInfoAdmin(admin.ModelAdmin):
    list_display = ['comment_man', 'comment_article', 'comment_content', 'add_time']
    fields = ['comment_man', 'comment_article', 'comment_content', 'add_time']


admin.site.register(ArticleInfo, ArticleInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TagInfo, TagInfoAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(CommentInfo, CommentInfoAdmin)
