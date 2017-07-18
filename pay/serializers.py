# coding=utf-8
from rest_framework import serializers


"""
    Author:	         马承成
    Version:         0.01v
    Date:            2017/03/30
    Description:     支付结果异步通知序列化
"""


class PayInfoSerializers(serializers.Serializer):
    # 原支付请求的商户订单号
    out_trade_no = serializers.CharField(max_length=64)
    # 实收金额
    receipt_amount = serializers.IntegerField()
    # 交易状态
    trade_status = serializers.CharField(max_length=32)
