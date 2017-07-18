# -*- coding: utf-8 -*-
from captcha import views
from django.conf.urls import url

urlpatterns = [
    url(r'^captcha/$', views.show_captcha),
]
