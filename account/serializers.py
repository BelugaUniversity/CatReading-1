# coding=utf-8
from rest_framework import serializers

from .models import User
from books.models import BookInfo, BooksContent

class UserLoginSerializer(serializers.Serializer):
    userName = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)


class UsernameCheckSerializer(serializers.Serializer):
    userName = serializers.CharField(max_length=30)


class CheckPhoneSerializer(serializers.Serializer):
     phone = serializers.CharField(max_length=11)


class UserRegisterSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=30, min_length=6)


class UserChaseBooksSerializer(serializers.Serializer):
    bookId = serializers.IntegerField(read_only=True)
    coverImg = serializers.ImageField(read_only=True)
    recentlyCharpterNumber = serializers.IntegerField(read_only=True)
    recentlyCharpter = serializers.CharField(max_length=20)
    lastReadCharpterNumber = serializers.IntegerField(read_only=True)
    lastReadCharpter = serializers.CharField(max_length=20)