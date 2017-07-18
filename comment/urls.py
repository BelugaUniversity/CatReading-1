# -*- coding: utf-8 -*-
import views
from django.conf.urls import url

urlpatterns = [
    url(r'^CommentViewAPI/', views.CommentViewAPI.as_view()),

    url(r'^CommentUserViewAPI/', views.CommentUserViewAPI.as_view()),

    url(r'^CommentBookViewAPI/', views.CommentBookViewAPI.as_view()),

    url(r'^CommentManagerViewAPI/', views.CommentManagerViewAPI.as_view()),
    
    url(r'^EditCommentManagerViewAPI/', views.EditCommentManagerViewAPI.as_view()),
]