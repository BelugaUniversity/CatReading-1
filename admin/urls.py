# -*- coding: utf-8 -*-
import views
from django.conf.urls import url

urlpatterns = [
    url(r'^createBook/$', views.createBookPage),
    url(r'^bookManager/$', views.BookManagerPage),
    url(r'^editbookinfo/[0-9]+/$', views.EditBookInfoPage),

    url(r'^publish/[0-9]+/$', views.PublishPage),
    url(r'^commentManager/[0-9]+/$', views.commentManagerPage),
    url(r'^WriteChapter/[0-9]+/$', views.WriteChaptersPage),

    url(r'^uploadimg/$', views.UploadImgPage),

    url(r'^userManager/$', views.UserManagerPage),

    url(r'^datastatistics/$', views.dataStatisticsPage),

    url(r'^admin/$', views.AdminLoginkPage),

    url(r'^CreateBookAPIView/', views.CreateBookAPIView.as_view()),
    url(r'^BookListAPIView/', views.BookListAPIView.as_view()),
    url(r'^CreateChapterAPIView/', views.CreateChapterAPIView.as_view()),
    url(r'^DeleteBookAPIView/', views.DeleteBookAPIView.as_view()),
    url(r'^ChaptersListAPIView/', views.ChaptersListAPIView.as_view()),
    url(r'^DeleteChapterAPIView/', views.DeleteChapterAPIView.as_view()),
    url(r'^ShowBookInfoAPIView/', views.ShowBookInfoAPIView.as_view()),
    url(r'^EditBookInfoAPIView/', views.EditBookInfoAPIView.as_view()),
    url(r'^EditChapterListAPIView/', views.EditChapterListAPIView.as_view()),
    url(r'^ShowChapterAPIView/', views.ShowChapterAPIView.as_view()),
    url(r'^WordCountAPIView/', views.WordCountAPIView.as_view()),
    url(r'^ReleaseChapterAPIView/', views.WordCountAPIView.as_view()),
    url(r'^CoverImgUploadAPIView/', views.CoverImgUploadAPIView.as_view()),
    url(r'^RecommendBookAPIView/', views.RecommendBookAPIView.as_view()),

    url(r'^ShowUserListAPIView/', views.ShowUserListAPIView.as_view()),
    url(r'^EditUserAPIView/', views.EditUserAPIView.as_view()),
]