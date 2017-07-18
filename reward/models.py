# **coding: utf-8**
from __future__ import unicode_literals
from django.db import models

"""
    Author:	         毛毛
    Version:         0.02v
    Date:            2017/03/30
    Description:     打赏信息信息模型
    history:
        <日期>           <描述>
        2017/04／26      添加书籍价格字段
"""


class Reward(models.Model):
    userId = models.IntegerField("用户id")
    bookId = models.IntegerField("书籍id")
    userName = models.CharField("用户名", max_length=30)
    bookName = models.CharField("书名", max_length=30)
    rewardType = models.IntegerField("奖励类型")
    rewardMoney = models.IntegerField("消费猫币")
    productionNumber = models.IntegerField("物品数量")
    rewardTime = models.DateTimeField("打赏日期", auto_now_add=True)