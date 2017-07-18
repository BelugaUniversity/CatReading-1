# **coding: utf-8**

from rest_framework import serializers
from .models import DayDataStatistics, MonthDataStatistics

"""
    Author:	         成成
    Version:         0.01v
    Date:            2017/05/01
    Description:     评论的数据序列化
"""


class DayDataStatisticsSerializers(serializers.ModelSerializer):
    produceDataDate = serializers.SerializerMethodField()

    class Meta:
        model = DayDataStatistics
        fields = ('id', 'produceDataDate', 'dayPVNumber', 'dayRechargeNumber', 'dayRewardNumber', 'dayLogonNumber', 'dayChaseBooksNumber',
                  'daySubscribersNumber')

    def get_produceDataDate(self, obj):
        return obj.produceDataDate.strftime("%Y/%m/%d")


class MonthDataStatisticsSerializers(serializers.ModelSerializer):
    produceDataDate = serializers.SerializerMethodField()

    class Meta:
        model = MonthDataStatistics
        fields = ('id', 'produceDataDate', 'monthPVNumber', 'monthRechargeNumber', 'monthRewardNumber', 'monthLogonNumber', 'monthChaseBooksNumber',
                  'monthSubscribersNumber')

    def get_produceDataDate(self, obj):
        return obj.produceDataDate.strftime("%Y/%m")


class LineCharDataStatisticsSerializers(serializers.ModelSerializer):
    produceDataDate = serializers.SerializerMethodField()

    class Meta:
        model = DayDataStatistics
        fields = ('produceDataDate', 'dayPVNumber', 'dayRewardNumber')

    def get_produceDataDate(self, obj):
        return obj.produceDataDate.strftime("%m月%d日")
