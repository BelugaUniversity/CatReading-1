# **coding: utf-8**

from rest_framework import serializers
from .models import Reward

"""
    Author:	         成成
    Version:         0.01v
    Date:            2017/05/01
    Description:     打赏的数据序列化
"""


class RewardSerializers(serializers.Serializer):
    # 用户ID
    # userId = serializers.IntegerField(read_only=True)
    # 书籍ID
    bookId = serializers.IntegerField(read_only=True)
    # 用户名
    userName = serializers.CharField(read_only=True)
    # 书名
    # bookName = serializers.CharField(read_only=True)
    # 打赏类型
    rewardType = serializers.IntegerField(read_only=True)
    # 打赏金额
    # rewardMoney = serializers.IntegerField(read_only=True)
    # 打赏数量
    productionNumber = serializers.IntegerField(read_only=True)
    # 评论时间
    # commentTime = serializers.DateTimeField(read_only=True)


class BookInfoRewardSerializers(serializers.ModelSerializer):

    class Meta:
        model = Reward
        fields = ('userName', 'productionNumber', 'rewardType')
