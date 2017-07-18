# **coding: utf-8**`
"""
    Copyright (c), 2016-2017,  beluga Tech.
    File name： view.py
    Description:  用户支模块
"""

from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from alipay import AliPay
from utils import shortcuts
from pay.serializers import PayInfoSerializers
import time
import random


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     读者支付页面
"""


def payContailPage(request):
    return render(request, "reading/pay/payContail.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     读者支付选择方式页面
"""


def payMentPage(request):
    return render(request, "reading/pay/payment.html")

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/04/18
    Description:     读者支付成功页面
"""


def paySuccessPage(request):
    return render(request, "reading/pay/paySuccess.html")

"""
    Author:	         马承成
    Version:         0.02v
    Date:            2017/07/07
    Description:     支付跳回页面
"""


class PayReturnURLAPIView(APIView):
    def get(self, request):
        print request.GET.get('trade_no')
        return render(request, "reading/pay/paySuccess.html")


"""
    Author:	         马承成
    Version:         0.02v
    Date:            2017/07/07
    Description:     接受支付宝的异步通知
"""


class PayNotifyURLAPIView(APIView):

    @ csrf_exempt
    def post(self, request):
        data = PayInfoSerializers(request.data)
        if data['trade_status'] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            print "success"
        return

"""
    Author:	         马承成
    Version:         0.02v
    Date:            2017/07/07
    Description:     支付的API接口
"""


class PayAPIView(APIView):

    def get(self, request):

        alipay = AliPay(
            appid="2016080600179942",
            app_notify_url="http://pay.beluga.studio/notify_url.php",
            app_private_key_path="/home/mcc/app_private_key.pem",
            alipay_public_key_path="/home/mcc/app_public_key.pem",
            sign_type="RSA2",
        )
        subject = u"猫币".encode("utf8")
        money = request.GET.get('money')
        out_trade_no = time.strftime("%H%M%S") + str(random.randint(1000, 9999))

        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=out_trade_no,
            total_amount=money,
            subject=subject,
            return_url="http://pay.beluag.studio/return_url.php"
        )

        message = u"https://openapi.alipaydev.com/gateway.do?"+order_string
        return shortcuts.success_response(message)
