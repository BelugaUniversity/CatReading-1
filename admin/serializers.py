# **coding: utf-8**
"""
    Copyright (c), 2016-2017,  beluga Tech.
    File name： view.py
    Description: 阅读应用模块的视图处理
"""

from books.models import BookInfo, BooksContent
from account.models import User, UserProfile
from rest_framework import serializers
from utils import booktype


class BookListSerializers(serializers.ModelSerializer):

    STATE_CHOICE = {0: "更新中", 1: "已完结"}

    type = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()

    class Meta:
        model = BookInfo
        fields = ('bookName', 'id', 'coverImg', 'author', 'subscribersNumber', 'chaptersNumber', 'type', 'state', 'testimonials',
                  'hotBook', 'freeBook', 'rankBook', 'newBook', 'headImgBook')

    def get_type(self, obj):
        return booktype.bookType[obj.type]

    def get_state(self, obj):
        return self.STATE_CHOICE[obj.state]

class CreateChapterSerializers(serializers.Serializer):

    bookId = serializers.IntegerField(read_only=True)
    chaptersId = serializers.IntegerField(read_only=True)
    chaptersName = serializers.CharField(max_length=30)
    chaptersType = serializers.IntegerField(read_only=True)
    chaptersContent = serializers.CharField()
    chaptersState = serializers.IntegerField(read_only=True)


class ChaptersListSerializers(serializers.ModelSerializer):
    updateTime = serializers.SerializerMethodField()

    class Meta:
        model = BooksContent
        fields = ('chaptersId', 'chaptersName', 'updateTime', 'chaptersPV', 'wordNumber', 'chaptersType')

    def get_updateTime(self, obj):
        return obj.updateTime.strftime("%Y-%m-%d")


class ShowBookInfoSerializers(serializers.ModelSerializer):

    class Meta:
        model = BookInfo
        fields = ('bookName', 'coverImg', 'author', 'chaseBooksNumber', 'wordNumber', 'state', 'type', 'describe', 'testimonials')


class EditBookInfoSerializers(serializers.ModelSerializer):

    class Meta:
        model = BookInfo
        fields = ('id', 'bookName', 'author', 'state', 'type', 'describe', 'testimonials')


class EditChapterListSerializers(serializers.ModelSerializer):
    updateTime = serializers.SerializerMethodField()

    class Meta:
        model = BooksContent
        fields = ('chaptersId', 'chaptersName', 'wordNumber', 'updateTime')

    def get_updateTime(self, obj):
        return obj.updateTime.strftime("%Y-%m-%d")


class ShowChapterSerializers(serializers.ModelSerializer):

    class Meta:
        model = BooksContent
        fields = ('chaptersName', 'chaptersType', 'chaptersContent', 'chaptersState')


class ShowUserListSerializers(serializers.ModelSerializer):
    # 注册时间
    registerTime = serializers.SerializerMethodField()
    # 推荐票
    recommendTicket = serializers.SerializerMethodField()
    # 钻石票
    diamondTicket = serializers.SerializerMethodField()
    # 猫币余额
    balance = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'userName', 'phone', 'diamondTicket', 'recommendTicket', 'balance', 'isForbidden', 'registerTime')

    def get_recommendTicket(self, obj):
        return obj.user_userprofile.get().recommendTicket

    def get_diamondTicket(self, obj):
        return obj.user_userprofile.get().diamondTicket

    def get_balance(self, obj):
        return obj.user_userprofile.get().balance

    def get_registerTime(self, obj):
        return obj.registerTime.strftime("%Y-%m-%d")



class RecommendBookSerializers(serializers.Serializer):
    # 热书推荐
    hotBook = serializers.IntegerField(read_only=True)
    # 免费精品
    freeBook = serializers.IntegerField(read_only=True)
    # 上架精品
    rankBook = serializers.IntegerField(read_only=True)
    # 新书推荐
    newBook = serializers.IntegerField(read_only=True)
    # 顶部书籍推荐
    headImgBook = serializers.IntegerField(read_only=True)
    # 推荐语
    testimonials = serializers.CharField(max_length=20)


