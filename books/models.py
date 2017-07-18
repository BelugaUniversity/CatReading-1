# **coding: utf-8**
from __future__ import unicode_literals

from django.db import models
import time

# Create your models here.

"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/03/30
    Description:     书籍基本信息数据模型
    history:
        <日期>           <描述>
        2017/04／26      添加书籍价格字段
"""


class BookInfo(models.Model):
    # 书籍类型选项
    BOOK_TYPE_CHOICES = (
        (1, "仙剑"),
        (2, "玄幻"),
        (3, "悬疑"),
        (4, "奇幻"),
        (5, "军事"),
        (6, "历史"),
        (7, "竞技"),
        (8, "科幻"),
        (9, "校园"),
        (10, "社会"),
        (11, "其它"),
    )

    # 书籍更新状态选项
    BOOK_STATE_CHOICE = (
        (0, "更新中"),
        (1, "已完成"),
    )
    # 作者
    author = models.CharField("作者", max_length=20, default="佚名")
    # 书名
    bookName = models.CharField("书名", max_length=20)
    # 书籍封面
    coverImg = models.ImageField("书籍封面", default="./2706179_185025082_2.jpg")
    # 书籍简介
    describe = models.TextField("书籍概要简介")
    # 书籍类型
    type = models.SmallIntegerField("书籍类型", default = 1, choices=BOOK_TYPE_CHOICES, name='type')
    # 书籍字数
    wordNumber = models.IntegerField("字数", default=0)
    # 更新状态
    state = models.SmallIntegerField("更新状态", default = 0, choices=BOOK_STATE_CHOICE)
    # 目前章节数量
    chaptersNumber = models.SmallIntegerField("更新章节数", default=0)
    # 书籍价格
    bookMoney = models.IntegerField("书籍价格", default=0)
    # 最近一次的更新时间
    updateTime = models.DateTimeField("更新时间", auto_now_add=True)
    # 点击量
    clicksNumber = models.IntegerField("点击量", default=0)
    # 订阅量
    subscribersNumber = models.IntegerField("订阅量", default=0)
    # 追书量
    chaseBooksNumber = models.IntegerField("追书量", default=0)
    # 猫币打赏总数
    reward = models.IntegerField("猫币打赏总数", default=0)
    # 猫球打赏总量
    catBallNumber = models.IntegerField("猫球打赏总量", default=0)
    # 猫薄荷打赏总量
    catnipNumber = models.IntegerField("猫薄荷打赏总量", default=0)
    # 逗猫棒打赏总量
    catStickNumber = models.IntegerField("逗猫棒打赏总量", default=0)
    # 猫粮打赏总量
    catFoodNumber = models.IntegerField("猫抓饭打赏总量", default=0)
    # 鱼打赏总量
    catFishNumber = models.IntegerField("跑爬架打赏总量", default=0)
    # 猫窝打赏总量
    catHouseNumber = models.IntegerField("猫窝打赏总量", default=0)
    # 热书推荐
    hotBook = models.IntegerField("热书推荐排行位数", default=0)
    # 免费精品
    freeBook = models.IntegerField("免费精品排行位数", default=0)
    # 上架精品
    rankBook = models.IntegerField("上架排行位数", default=0)
    # 新书推荐
    newBook = models.IntegerField("新书推荐排行位数", default=0)
    # 顶部书籍推荐
    headImgBook = models.IntegerField("顶部书籍推荐排行位数", default=0)
    # 推荐语
    testimonials = models.CharField("推荐语", max_length=20, default="")

    def add_clicks_number(self):
        self.clicksNumber += 1

    def add_subscriber_number(self):
        self.subscribersNumber += 1

    def add_chase_number(self):
        self.chaseBooksNumber += 1

    def add_chapters_number(self):
        self.chaptersNumber += 1
        self.save()

    def subtract_chapters_number(self):
        self.chaptersNumber -= 1
        self.save()

    class Meta:
        db_table = "book_info"


"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/03/30
    Description:     书籍内容模型
    history:
        <日期>　　　　    <描述>                <修改人>
        2017/04／26      添加章节价格字段        马承成
        2017/04／26      添加章节价格类型        马承成
"""


class BooksContent(models.Model):

    # 书籍章节类型选项
    CHAPTER_TYPE_CHOICE = (
        (0, "免费"),
        (1, "收费"),
    )

    # 书籍章节状态选项
    CHAPTER_STATE_CHOICE = (
        (0, "不发布"),
        (1, "发布"),
    )

    # 对应的图书ID
    BookInfo =models.ForeignKey(BookInfo, related_name='bookinfo_bookscontent', verbose_name="书本ID")
    # 章节数
    chaptersId = models.SmallIntegerField("章节数")
    # 章节名称
    chaptersName = models.CharField("章节名称", max_length=20)
    # 该章节的内容
    chaptersContent = models.TextField("章节内容")
    # 章节字数
    wordNumber = models.IntegerField("章节字数", default=0)
    # 改章节更新时间
    updateTime = models.DateTimeField("章节更新时间", auto_now_add=True)
    # 章节类型
    chaptersType = models.IntegerField("章节类型", default=0, choices=CHAPTER_TYPE_CHOICE)
    # 章节状态
    chaptersState = models.IntegerField("章节类型", default=0, choices=CHAPTER_STATE_CHOICE)
    # 章节价钱
    chaptersMoney = models.IntegerField("章节价钱", default=0)
    # 章节浏览量
    chaptersPV = models.IntegerField("章节浏览量", default=0)

    class Meta:
        db_table = "book_content"
