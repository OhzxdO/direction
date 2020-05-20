from django.contrib import admin

# Register your models here.
from .models import words
from .models import classfications

class WordAdmin(admin.ModelAdmin):
    # 列表属性
    list_display = ['word','sound','plain','example','classfication']
    # 过滤器：进行单词分类筛选
    list_filter = ['classfication']
    # 单词搜素
    search_fields = ['word']
    # 每页显示数量
    list_per_page = 10
    # 级联查询
    list_select_related=['classfication']

class ClassAdmin(admin.ModelAdmin):
    # 列表属性
    list_display = ['pk','classfication']
    search_fields = ['classfication']
    list_per_page = 10

# 注册
admin.site.register(words,WordAdmin)
admin.site.register(classfications,ClassAdmin)
admin.site.site_header = "HJJ词典"
admin.site.site_title = "HJJ词典"
