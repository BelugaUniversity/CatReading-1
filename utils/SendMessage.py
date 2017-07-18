# -*- coding: utf-8 -*-
import top.api


def SendMessage(phone, code):
    phone = str(phone)
    appkey = "23368540"
    secret = "ada606d5b7d446e0d4173348e0af1044"

    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(appkey, secret))

    req.sms_type = "normal"
    req.sms_free_sign_name = "袋鼠账号"
    req.sms_param = "{\"code\":\"" + code + "\",\"product\":\"猫阅读\"}"
    req.rec_num = phone
    req.sms_template_code = "SMS_9680408"
    try:
        resp = req.getResponse()
        return resp
    except Exception, e:
        return e

# SendMessage("15623637978", "3030")
