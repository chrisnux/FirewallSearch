# Register your models here.
# 注册站点到后台管理
from django.contrib import admin
from .models import Question,Choice

admin.site.register(Question)
admin.site.register(Choice)