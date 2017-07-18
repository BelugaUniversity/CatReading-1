# **coding: utf-8**
from django.http import QueryDict

class Reward:
    def __init__(self, name, money):
        self.name = name
        self.money = money

rewardType = QueryDict(mutable=True)
rewardType['1'] = Reward('猫球', 100)
rewardType['2'] = Reward('猫薄荷', 500)
rewardType['3'] = Reward('逗猫棒', 1000)
rewardType['4'] = Reward('鱼', 3000)
rewardType['5'] = Reward('猫粮', 5000)
rewardType['6'] = Reward('猫窝', 10000)

