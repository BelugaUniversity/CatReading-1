# -*- coding: utf-8 -*-
"""CatReading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import books
import account
import admin
import reward
import utils
import comment
import statistics
import pay
from django.conf.urls import url, include
from books import urls
from account import urls
from admin import urls
from reward import urls
from comment import urls
from pay import urls
from statistics import urls
from utils import urls


urlpatterns = [
    # 打赏URL配置
    # “r”避免转义
    url(r'^', include(reward.urls), name='reward_URLconf'),

    # 后台管理URL配置
    url(r'^', include(admin.urls), name='admin_URLconf'),

    # 后台管理URL配置
    url(r'^', include(account.urls), name='account_URLconf'),

    # 书籍URL配置
    url(r'^', include(books.urls), name='books_URLconf'),

    # 评论URL配置
    url(r'^', include(comment.urls), name='books_URLconf'),

    # 支付URL配置
    url(r'^', include(pay.urls), name='books_URLconf'),

    # 工具URL配置
    url(r'^', include(utils.urls), name='utils_URLconf'),

    # 数据统计URL配置
    url(r'^', include(statistics.urls), name='utils_URLconf')

]
