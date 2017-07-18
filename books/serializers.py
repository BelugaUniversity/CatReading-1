# **coding: utf-8**
"""
    Copyright (c), 2016-2017,  beluga Tech.
    File name： view.py
    Description: 阅读应用模块的视图处理
"""

from .models import BookInfo, BooksContent
from rest_framework import serializers
from utils import booktype


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     榜单列表的数据序列化
"""


class CompetitiveListSerializers(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = BookInfo
        fields = ('bookName', 'testimonials', 'id', 'type')

    def get_type(self, obj):
        return booktype.bookType[obj.type]


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     排行榜列表的数据序列化
"""


class RankListSerializers(serializers.Serializer):
    # 书籍ID
    id = serializers.IntegerField(read_only=True)
    # 书籍名
    bookName = serializers.CharField(max_length=20, read_only=True)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     图片与书名的数据序列化
"""


class ShowImgSerializers(serializers.Serializer):
    # 书籍ID
    id = serializers.IntegerField(read_only=True)
    # 封面
    coverImg = serializers.ImageField(read_only=True)
    # 书名
    bookName = serializers.CharField(max_length=20, read_only=True)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     详情页头部的数据序列化
"""


class BookHeadInfoSerializers(serializers.Serializer):
    # 书籍ID
    id = serializers.IntegerField(read_only=True)
    # 封面
    coverImg = serializers.ImageField(read_only=True)
    # 书名
    bookName = serializers.CharField(max_length=30, read_only=True)
    # 总字数
    wordNumber = serializers.IntegerField(read_only=True)
    # 作者名：
    author = serializers.CharField(max_length=20, read_only=True)
    # 点击量
    clicksNumber = serializers.IntegerField(read_only=True)
    # 书迷
    subscribersNumber = serializers.IntegerField(read_only=True)
    # 状态
    state = serializers.IntegerField(read_only=True)


class BookInfoSerializers(serializers.ModelSerializer):

    STATE_CHOICE = {0: "更新中", 1: "已完结"}

    chaptersName = serializers.SerializerMethodField()
    chaptersId = serializers.SerializerMethodField()
    updateTime = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()

    class Meta:
        model = BookInfo
        fields = ('id', 'coverImg', 'bookName', 'wordNumber', 'author', 'clicksNumber', 'subscribersNumber', 'state',
                  'reward', 'catBallNumber', 'catnipNumber', 'catStickNumber', 'catFoodNumber', 'catFishNumber',
                  'catHouseNumber', 'chaptersName', 'chaptersId', 'updateTime')

    def get_chaptersName(self, obj):
        return obj.bookinfo_bookscontent.get(chaptersId=obj.chaptersNumber).chaptersName

    def get_chaptersId(self, obj):
        return obj.bookinfo_bookscontent.get(chaptersId=obj.chaptersNumber).chaptersId

    def get_updateTime(self, obj):
        return obj.bookinfo_bookscontent.get(chaptersId=obj.chaptersNumber).updateTime.strftime("%m-%d %H:%M")

    def get_state(self, obj):
        return self.STATE_CHOICE[obj.state]


class LibrarySerializers(serializers.ModelSerializer):
    # chaptersName = serializers.SerializerMethodField()
    # updateTime = serializers.SerializerMethodField()

    class Meta:
        model = BookInfo
        fields = ('id', 'wordNumber', 'author',
                  'chaptersNumber', 'bookName')

    # def get_chaptersName(self, obj):
    #     return obj.bookinfo_bookscontent.get(chaptersId=obj.chaptersNumber).chaptersName

    # def get_updateTime(self, obj):
    #     return obj.bookinfo_bookscontent.get(chaptersId=obj.chaptersNumber).updateTime.strftime("%m-%d %H:%M")


"""
        Author:	         毛毛
        Version:         0.01v
        Date:            2017/04/03
        Description:     详情页尾部的数据序列化
"""


class ChaptersSerializers(serializers.Serializer):
    # 书籍ID
    id = serializers.IntegerField(read_only=True)
    # 章节数
    chaptersId = serializers.IntegerField(read_only=True)
    # 章节名
    chaptersName = serializers.CharField(max_length=20, read_only=True)

"""
        Author:	         毛毛
        Version:         0.01v
        Date:            2017/07/07
        Description:     搜索页书籍的序列化
"""


class SearchBooksSerializers(serializers.Serializer):
    # 书名
    bookName = serializers.CharField(max_length=20,read_only=True)
    # 章节数
    chaptersNumber = serializers.IntegerField(read_only=True)
    # 章节名
    chaptersName = serializers.CharField(max_length=20, read_only=True)
    # 作者
    author = serializers.CharField(max_length=20,read_only=True)
    # 字数
    wordNumber = serializers.IntegerField(read_only=True)
    # 更新时间
    updateTime = serializers.DateTimeField(read_only=True)