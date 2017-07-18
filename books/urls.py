# -*- coding: utf-8 -*-
import views
from django.conf.urls import url

urlpatterns = [
    # 首页
    url(r'^$', views.indexPage, name='index'),
    # 书库页
    url(r'^library/', views.libraryPage, name='library'),
    # 排行页
    url(r'^rank/', views.rankPage, name='rank'),

    # 搜书页
    url(r'^search/', views.searchPage, name='rank'),

    # 详情页
    url(r'^bookDetails/', views.bookDetailsPage, name='bookDetails'),
    url(r'^catalogue/[0-9]+/$', views.cataloguePage, name='catalogue'),
    url(r'^bookCommentInfo/[0-9]+/$', views.bookCommentPage, name='bookCommentPage'),
    url(r'^bookRewardInfo/[0-9]+/$', views.bookRewardPage, name='bookRewardPage'),

    # 详情页
    url(r'^books/[0-9]+/$', views.bookDetailsPage, name='bookDetails'),
    url(r'^books/[0-9]+/chapters/[0-9]+/$', views.readingPage, name='Reading'),

    # 首页API请求接口
    url(r'^ShowImgViewAPI/', views.ShowImgViewAPI.as_view()),
    url(r'^FreeCompetitiveViewAPI/', views.FreeCompetitiveViewAPI.as_view()),
    url(r'^GroundCompetitiveViewAPI/', views.GroundCompetitiveViewAPI.as_view()),
    url(r'^HotRecommendViewAPI/', views.HotRecommendViewAPI.as_view()),
    url(r'^NewRecommendViewAPI/', views.NewRecommendViewAPI.as_view()),
    url(r'^LibraryViewAPI/', views.LibraryAPIView.as_view()),
    # 排行页API请求接口
    url(r'^RankListViewAPI/', views.RankListViewAPI.as_view()),
    # 详情页API请求接口
    url(r'^ChaptersViewAPI/', views.ChaptersViewAPI.as_view()),
    url(r'^BookInfoHeadViewAPI/', views.BookInfoHeadViewAPI.as_view()),

    url(r'^BookInfoViewAPI/', views.BookInfoViewAPI.as_view()),

    # 阅读页面API请求接口
    url(r'^ReadingViewAPI/', views.ReadingViewAPI),


    url(r'^chaseBooksAPIView/', views.chaseBooksAPIView.as_view()),
    url(r'^subscribersAPIView/', views.subscribersAPIView.as_view()),

    url(r'^searchBooksViewAPI/', views.searchBooksViewAPI.as_view()),


]
