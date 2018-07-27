from django.contrib import admin
from .models import BanClass, StudentInfo, CardId


# Register your models here.
class StudentInfoInlineAdmin(admin.TabularInline):
    model = StudentInfo
    extra = 0
    # extra = 3


class CardIdInlineAdmin(admin.TabularInline):
    model = CardId


class BanClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_time']
    list_per_page = 10
    search_fields = ['name']
    list_filter = ['name', 'add_time']
    fields = ['add_time', 'name']
    inlines = [StudentInfoInlineAdmin]


class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'age', 'stu_ban', ]
    list_per_page = 10
    search_fields = ['name', 'age', 'gender']
    list_filter = ['name', 'gender', 'age']
    fields = ['name', 'age', 'stu_ban', 'gender']
    inlines = [CardIdInlineAdmin]
    # inlines = [BanClassInlineAdmin]   #只能在主模型中嵌入子模型，有关系字段的相对来说是子模型


class CardIdAdmin(admin.ModelAdmin):
    list_display = ['id_number', 'stu_card']
    list_per_page = 10
    search_fields = ['id_number']
    list_filter = ['id_number', 'stu_card']
    fields = ['stu_card', 'id_number']


admin.site.register(BanClass, BanClassAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(CardId, CardIdAdmin)
