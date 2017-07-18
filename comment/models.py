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


class Comment(models.Model):

    # 书籍更新状态选项
    COMMENT_TYPE_CHOICE = (
        (0, "一般"),
        (1, "精华"),
        (2, "置顶"),
        (3, "精华并置顶"),
    )

    userId = models.IntegerField("用户id", default=0)
    bookId = models.IntegerField("书籍id")
    userName = models.CharField("用户名", max_length=30)
    bookName = models.CharField("书名", max_length=30)
    commentType = models.IntegerField("评论类型", choices=COMMENT_TYPE_CHOICE, default=0)
    commentStick = models.BooleanField("书籍置顶", default=False)
    commentEssence = models.BooleanField("书籍精华", default=False)
    commentTitle = models.CharField("评论标题", max_length=20)
    commentContent = models.CharField("评论内容", max_length=120)
    commentTime = models.DateTimeField("评论时间", auto_now_add=True)
    isShow = models.BooleanField("评论是否显示", default=False)
