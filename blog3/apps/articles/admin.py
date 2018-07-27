from django.contrib import admin
from .models import Category, ArticleInfo, TagInfo, ArticleTags, CommentInfo


# Register your models here.


class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'content', 'author', 'image', 'category',
                    'click_num', 'love_num', 'comment_num', 'add_time']
    fields = ['title', 'desc', 'content', 'author', 'image', 'category',
              'click_num', 'love_num', 'comment_num', 'add_time']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_time']
    fields = ['add_time', 'name']


class TagInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_time']
    fields = ['add_time', 'name']


class ArticleTagsAdmin(admin.ModelAdmin):
    list_display = ['article_info', 'tag_info', 'add_time']
    fields = ['article_info', 'tag_info', 'add_time']


class CommentInfoAdmin(admin.ModelAdmin):
    list_display = ['comment_man', 'comment_article', 'comment_content', 'add_time']
    fields = ['comment_man', 'comment_article', 'comment_content', 'add_time']


admin.site.register(ArticleInfo, ArticleInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ArticleTags, ArticleTagsAdmin)
admin.site.register(TagInfo, TagInfoAdmin)
admin.site.register(CommentInfo, CommentInfoAdmin)
