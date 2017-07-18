# **coding: utf-8**
from __future__ import unicode_literals
from account.models import User
from reward.models import Reward
from django.db import models

class DayDataStatistics(models.Model):
    # 日浏览量
    dayPVNumber = models.IntegerField(default=0)
    # 日充值
    dayRechargeNumber = models.IntegerField(default=0)
    # 日打赏量
    dayRewardNumber = models.IntegerField(default=0)
    # 日注册量
    dayLogonNumber = models.IntegerField(default=0)
    # 日追书量
    dayChaseBooksNumber = models.IntegerField(default=0)
    # 日订阅量
    daySubscribersNumber = models.IntegerField(default=0)
    # 日期
    produceDataDate = models.DateField(auto_now_add=True)
    class Meta:
        db_table = "DayDataStatistics"


class MonthDataStatistics(models.Model):
    # 月浏览量
    monthPVNumber = models.IntegerField(default=0)
    # 月充值
    monthRechargeNumber = models.IntegerField(default=0)
    # 月打赏量
    monthRewardNumber = models.IntegerField(default=0)
    # 月注册量
    monthLogonNumber = models.IntegerField(default=0)
    # 月追书量
    monthChaseBooksNumber = models.IntegerField(default=0)
    # 月订阅量
    monthSubscribersNumber = models.IntegerField(default=0)
    # 日期
    produceDataDate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "MonthDataStatistics"


def TotalPVNumber():
    totalPVNumber = 0
    daysDatas = DayDataStatistics.objects.all()
    for dayData in daysDatas:
        totalPVNumber += dayData.dayPVNumber
    return totalPVNumber

def TotalLogonNumber():
    totalLogonNumber = User.objects.all().count()
    return totalLogonNumber

def TotalRewardNumber():
    totalRewardNumber = 0
    rewards = Reward.objects.all()
    for reward in rewards:
        totalRewardNumber += reward.rewardMoney
    return totalRewardNumber


def PropsNumber(rewardType):
    propsNumber = 0
    rewards = Reward.objects.filter(rewardType=rewardType).all()
    for reward in rewards:
        propsNumber += reward.productionNumber
    return propsNumber

# TotalPVNumber: 0,
# TotalRegisterNumber: 0,
# TotalRewardNumber: 0,
# TotalCatBallNumber: 0,
# TotalCatnipNumber: 0,
# TotalCatStickNumber: 0,
# TotalCatFoodNumber: 0,
# TotalCatFishNumber: 0,
# TotalCatHouseNumber: 0,