# **coding: utf-8**`
"""
    Copyright (c), 2016-2017,  beluga Tech.
    File name： view.py
    Description: 用户应用模块的视图处理
"""

import random
import json
from django.shortcuts import render
from django.http import QueryDict, HttpResponse,HttpResponseRedirect
from rest_framework.views import APIView
from .serializers import UserLoginSerializer, UserRegisterSerializer, UserChaseBooksSerializer
from books.serializers import ShowChaseBooksSerializers
from comment.serializers import CommentUserSerializers
from django.contrib import auth
from .models import User
from books.models import BooksChase, BooksSubscribe
from comment.models import Comment
from utils import SendMessage, shortcuts
from utils.captcha import Captcha
from django.views.decorators.csrf import csrf_exempt
from account.models import UserChaseBooks, UserProfile
from account.decorators import admin_required
from alipay import AliPay
import time
import random

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


class UserLoginAPIView(APIView):

    @csrf_exempt
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            print data
            user = auth.authenticate(userName=data["userName"], password=data["password"])
            if user:
                auth.login(request, user)
                message = "登录成功"
                print message
                return shortcuts.success_response(message)
            else:
                message = "您输入的帐号密码不正确，请重新输入"
                print message
                return shortcuts.error_response(message)
        else:
            message = "请输入正确格式"
            print message
            return shortcuts.error_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


class UserLogoutAPIView(APIView):

    def get(self, request):
        auth.logout(request)
        message = u"成功推出"
        return shortcuts.success_response(message)


class UserRegisterAPIView(APIView):

    @csrf_exempt
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        data = request.data
        phone = request.session.get('phone')

        if serializer.is_valid():
            user = User.objects.create(userName=phone)
            user.set_password(data["password"])
            user.phone = phone
            user.save()
            userProfile = UserProfile(User=user)
            userProfile.save()
            message = "注册成功"
            return shortcuts.success_response(message)
        else:
            message = "请输入正确格式"
            return shortcuts.error_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def CheckPhone(phone):

    try:
        User.objects.get(phone=phone)
        return True
    except User.DoesNotExist:
        return False

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def SendMessageBefore(phone, request):
    request.session['phone'] = phone
    message = "手机号可用"
    token = repr(random.randint(1000, 9999))
    request.session['token'] = token
    SendMessage.SendMessage(phone, token)
    return shortcuts.success_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


class MessageAPIView(APIView):
    def get(self, request):
        phone = request.GET.get("phone")
        send_captcha = request.GET.get("captcha")
        pageSate = int(request.GET.get("pageState"))

        captcha = Captcha(request)

        if not captcha.check(send_captcha):
            message = "验证码错误"
            return shortcuts.error_response(message)
        else:
            # 号码存在
            if CheckPhone(phone):
                # 页面为找回
                if pageSate == 1:
                    return SendMessageBefore(phone, request)
                # 页面为注册
                else:
                    message = "手机号已注册"
                    return shortcuts.error_response(message)
            # 号码不存在
            else:
                # 页面为注册
                if pageSate == 0:
                    return SendMessageBefore(phone, request)
                # 页面为找回0
                else:
                    message = "用户不存在"
                    return shortcuts.error_response(message)





"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


class CheckTokenAPIView(APIView):

    def get(self, request):

        session_token = request.session.get('token')
        token = request.GET.get("token")
        if session_token == token:
            message = "验证通过"
            return shortcuts.success_response(message)
        else:
            message = "短信验证码无效，请稍后点击重新发送短信"
            return shortcuts.error_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


class CheckUserNameAPIView(APIView):
    def get(self, request):
        userName = request.GET.get("userName")
        try:
            User.objects.get(userName=userName)
            message = "用户名可用"
            return shortcuts.success_response(message)
        except User.DoesNotExist:
            message = "用户名已被注册，请换其他用户名进行注册"
            return shortcuts.error_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


class ChangePasswordAPIView(APIView):

    @csrf_exempt
    def post(self, request):
        phone = request.session.get('phone')
        password = request.POST.get("password")
        user = User.objects.filter(phone=phone).get()
        user.set_password(password)
        user.save()
        message = "密码修改成功"
        return shortcuts.success_response(message)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/05/19
    Description:     个人中心的渲染
"""


class UserCenterAPIView(APIView):

    def get(self, request):
        userId = request.user.id
        book = UserChaseBooks.objects.filter(userId=userId).all()

        userpro = UserProfile.objects.filter(User=request.user).get()
        comment = Comment.objects.filter(userId=userId).all()
        userserializer = UserChaseBooksSerializer(book, many=True)
        commentserializer = CommentUserSerializers(comment, many=True)
        center = QueryDict(mutable=True)
        center['userRunBook'] = userserializer.data
        center['balance'] = userpro.balance
        center['diamondTicket'] = userpro.diamondTicket
        center['recommendTicket'] = userpro.recommendTicket
        center['bookComment'] = commentserializer.data
        return HttpResponse(json.dumps(center.dict()))

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/09/16
    description:      用户追书
"""


class ShowBooksChaseViewAPI(APIView):
    def get(self, request):
        # userId = User.request.userId
        books = BooksChase.objects.filter(userId=1).all()
        serializers = ShowChaseBooksSerializers(books, many=True)
        chaseBook = QueryDict(mutable=True)
        chaseBook['list'] = serializers.data
        return HttpResponse(json.dumps(chaseBook.dict()))


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/09/16
    Description:     用户订阅
"""


class ShowSubscribeBooksViewAPI(APIView):
    def get(self, request):
        # userId = User.request.userId
        books = BooksSubscribe.objects.filter(userId=1).all()
        serializers = ShowChaseBooksSerializers(books, many=True)
        subscribe = QueryDict(mutable=True)
        subscribe['list'] = serializers.data
        return HttpResponse(json.dumps(subscribe.dict()))



"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def userCenterPage(request):
    return render(request, "reading/account/concret.html")



"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     历史评论界面
"""


def userHistoryCommentPage(request):
    return render(request, "reading/account/ownComment.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def loginPage(request):
    return render(request, "reading/account/login.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def oneRegisterPage(request):
    return render(request, "reading/account/oneRegister.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def twoRegisterPage(request):
    return render(request, "reading/account/twoRegister.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def threeRegisterPage(request):
    return render(request, "reading/account/threeRegister.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def oneFindPage(request):
    return render(request, "reading/account/oneFind.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def twoFindPage(request):
    return render(request, "reading/account/twoFind.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def threeFindPage(request):
    return render(request, "reading/account/threeFind.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     免费板块的视图渲染应用
"""


def fourFindPage(request):
    return render(request, "reading/account/fourFind.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     读者注册协议页面
"""


def readerAgreementPage(request):
    return render(request, "reading/account/readerAgreement.html")
