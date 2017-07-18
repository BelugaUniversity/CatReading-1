# -*- coding: utf-8 -*-
import views
from django.conf.urls import url

urlpatterns = [
    url(r'^DataStaticsAPIView/$', views.DataStaticsAPIView.as_view()),
]
