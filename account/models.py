# **coding: utf-8**
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class UserManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, userName):
        return self.get(**{self.model.USERNAME_FIELD: userName})


REGULAR_USER = 0
ADMIN = 1


class User(AbstractBaseUser):
    # 用户名
    userName = models.CharField(max_length=32, unique=True)
    # 电话号码
    phone = models.CharField(max_length=11, unique=True)
    # 是否可用
    is_active = models.BooleanField(default=True)
    # 用户注册时间
    registerTime = models.DateTimeField(auto_now_add=True, null=True)
    # 0代表不是管理员 1是普通管理员 2是超级管理员
    adminType = models.IntegerField(default=0)
    # 找回密码用的token
    resetPasswordToken = models.CharField(max_length=40, blank=True, null=True)
    # token 生成时间
    resetPasswordTokenCreateTime = models.DateTimeField(blank=True, null=True)
    # 是否禁用
    isForbidden = models.BooleanField(default=False)

    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "user"

    def get_full_name(self):
        return self.userName

    def get_short_name(self):
        return self.userName


class UserProfile(models.Model):
    # 以用户为外键
    User = models.ForeignKey(User, related_name='user_userprofile')
    # 推荐票
    recommendTicket = models.IntegerField("推荐票", default=0)
    # 钻石票
    diamondTicket = models.IntegerField("钻石票", default=0)
    # 猫币余额
    balance = models.IntegerField("猫币余额", default=0)
    # 最近阅读书籍id
    lastReadBook = models.IntegerField("最近阅读书籍Id", default=0)


"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/05/19
    Description:     书库模型

"""





class UserChaseBooks(models.Model):
    # 用户Id
    userId = models.IntegerField("用户ID", default=True)
    # 书籍名
    bookName = models.CharField("书籍名称", max_length=20)
    # 书籍图片
    coverImg = models.ImageField("书籍封面", default="./2706179_185025082_2.jpg")
    # 最新更新的章节数
    recentlyCharpterNumber = models.IntegerField("最新更新章节数", default=0)
    # 最新章节
    recentlyCharpter = models.CharField("最新的章节", max_length=20)
    # 上次阅读的章节数
    lastReadCharpterNumber = models.IntegerField("上次阅读的章节数", default=0)
    # 上次阅读的章节
    lastReadCharpter = models.CharField("上次阅读的章节", max_length=20)


class UserSubscribersBooks(models.Model):
    # 用户Id
    userId = models.IntegerField("用户ID", default=True)
    # 书籍名
    bookName = models.CharField("书籍名称", max_length=20)
    # 书籍图片
    coverImg = models.ImageField("书籍封面", default="./2706179_185025082_2.jpg")
    # 最新更新的章节数
    recentlyCharpterNumber = models.IntegerField("最新更新章节数", default=0)
    # 最新章节
    recentlyCharpter = models.CharField("最新的章节", max_length=20)
    # 上次阅读的章节数
    lastReadCharpterNumber = models.IntegerField("上次阅读的章节数", default=0)
    # 上次阅读的章节
    lastReadCharpter = models.CharField("上次阅读的章节", max_length=20)