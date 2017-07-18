# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
"""
    Author:	         马承成
    Version:         0.02v
    Date:            2017/07/07
    Description:     书籍购买订单数据模型
"""


class PayInfo(models.Model):
    # 原支付请求的商户订单号
    out_trade_no = models.CharField(max_length=64)
    # 实收金额
    receiptAmount = models.IntegerField()
    # 交易付款时间
    gmtPayment = models.DateTimeField(auto_created=True)
    # 用户电话号码
    user = models.IntegerField(max_length=16)
