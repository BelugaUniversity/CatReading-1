# -*- coding: utf-8 -*-
import views
from django.conf.urls import url

urlpatterns = [
    url(r'^payContail/$', views.payContailPage),
    url(r'^payMent/$', views.payMentPage),
    url(r'^paySuccess/$', views.paySuccessPage),
    url(r'^PayAPIView/$', views.PayAPIView.as_view()),
    url(r'^PayReturnURLAPIView/$', views.PayReturnURLAPIView.as_view()),
    url(r'^PayNotifyURLAPIView/$', views.PayNotifyURLAPIView.as_view()),
]
