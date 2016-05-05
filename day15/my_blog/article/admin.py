from django.contrib import admin
from article.models import UserProfile,HostProfile
# Register your models here.

# django.contrib 管理工具所在模块
# django.contrib.admin 管理工具
# django.contrib.auth 用户鉴别系统
# django.contrib.sessions 匿名会话
# django.contrib.comments 评论系统


admin.site.register(UserProfile)
admin.site.register(HostProfile)