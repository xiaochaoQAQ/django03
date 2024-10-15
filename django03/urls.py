"""
URL configuration for django03 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('testblog/', include('testblog.urls'))
"""
from lib2to3.fixes.fix_input import context

from django.contrib import admin
from django.urls import path

import testblog.views

urlpatterns = [
    # path('', testblog.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('newslist/',testblog.views.getNews,name='newslist'),
    path('',testblog.views.myhome),  # 网站首页
    path('aboutme/',testblog.views.aboutme),  # 关于我
    path('register/',testblog.views.register,name='register'),  # 注册
    path('register/add/',testblog.views.regadd),  # 注册用户功能接口
    path('userlist/<str:curpage>/',testblog.views.userlist),  # 用户列表
    path('userlist/edit/',testblog.views.useredit),  # 用户编辑
    path('userlist/edit/action/', testblog.views.useredit_action),  # 数据库中用户修改
    path('userlist/del/<str:userid>/', testblog.views.userdel_action),  # 数据库中删除页面的url功能

]
