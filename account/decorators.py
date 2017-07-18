# coding=utf-8
import functools
from rest_framework.response import Response
from django.http import HttpResponse


class BasePermissionDecorator(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type):
        return functools.partial(self.__call__, obj)

    def __call__(self, *args, **kwargs):
        if len(args) == 2:
            self.request = args[1]
        else:
            self.request = args[0]

        if self.check_permission():
            if self.request.user.isForbidden is True:
                if self.request.is_ajax():
                    message = u"您已被禁用,请联系管理员"
                    return Response(data={"code": 0, "data": message})
                else:
                    message = u"您已被禁用,请联系管理员"
                    return Response(data={"code": 0, "data": message})
            return self.func(*args, **kwargs)
        else:
            message = "请先登录!"
            url = "/login/"
            return Response(data={"code": 1, "data": message, "url": url})

    def check_permission(self):
        raise NotImplementedError()


class login_required(BasePermissionDecorator):
    def check_permission(self):
        return self.request.user.is_authenticated()


class admin_required(BasePermissionDecorator):
    def check_permission(self):
        return self.request.user.is_authenticated() and self.request.user.adminType == 1