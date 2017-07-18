# !/bin/bash
# 在Ubuntu 16.04 64位环境下

# 软件源的更新以及升级
sudo apt-get update
sudo apt-get upgrade

# 下载python以及python的版本控制工具pip
sudo apt-get install python-pip python

# 安装mysql数据库
sudo apt-get install mysql-server

# 安装uwsgi服务器
sudo pip install Uwsgi==2.0.14

# 安装django框架
sudo pip install django==1.9.0

# 安装django-restframework框架
sudo pip install djangorestframework==3.2.5





