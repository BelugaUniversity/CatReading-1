# **coding=utf-8**
from rest_framework.response import Response
import hashlib
import os

def success_response(data):
    return Response(data={"code": 0, "data": data})


def error_response(data):
    return Response(data={"code": 1, "data": data})


def rand_str(length=32):
    if length > 128:
        raise ValueError("length must <= 128")
    return hashlib.sha512(os.urandom(128)).hexdigest()[0:length]