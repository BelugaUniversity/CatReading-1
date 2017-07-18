# -*- coding: utf-8 -*-
import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', views.loginPage),
    url(r'^center/$', views.userCenterPage),
    url(r'^userHistoryComment/$', views.userHistoryCommentPage),

    url(r'^oneRegister/', views.oneRegisterPage),
    url(r'^twoRegister/', views.twoRegisterPage),
    url(r'^threeRegister/$', views.threeRegisterPage),
    url(r'^readerAgreement/$', views.readerAgreementPage),

    url(r'^oneFind/$', views.oneFindPage),
    url(r'^twoFind/$', views.twoFindPage),
    url(r'^threeFind/$', views.threeFindPage),
    url(r'^fourFind/$', views.fourFindPage),

    # 用户注册API请求接口
    url(r'^UserRegisterAPIView/', views.UserRegisterAPIView.as_view()),
    url(r'^UserLogoutAPIView/', views.UserLogoutAPIView.as_view()),
    # 用户登陆API请求接口
    url(r'^UserLoginAPIView/', views.UserLoginAPIView.as_view()),
    # 用户改变密码API请求接口
    url(r'^ChangePasswordAPIView/', views.ChangePasswordAPIView.as_view()),
    # 短信发送API请求接口
    url(r'^MessageAPIView/', views.MessageAPIView.as_view()),
    # 检查手机验证码API请求接口
    url(r'^CheckTokenAPIView/', views.CheckTokenAPIView.as_view()),

    url(r'^UserCenterAPIView/', views.UserCenterAPIView.as_view()),
]
