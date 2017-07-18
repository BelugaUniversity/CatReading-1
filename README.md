# 猫阅读网站


## **开发环境以及开发工具说明**
Ubuntu 16.04 64位
<br>
* pip 9.01
* Nginx 1.10.0
* Uwsgi 2.0.14
* Python 2.7.12
* Django 1.9.0
* djangorestframework 3.2.5
* MySQL 5.7.16
* python-alipay-sdk (1.1.0)

开发工具
<br>
* pycharm community edition
* Navicat for MySQL


## **项目目录** 
	.
	├── CatReading
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	├── manage.py
	├── README.md			// 说明文件
	├── static			// 静态文件目录
	│   └── src
	│       ├── css			// css文件目录
	│       ├── img			// 图片文件目录
	│       └── js			// js文件目录
	│           ├── app
	│           └── lib
	└── template			// 网页模板目录
	    └── src
		├── admin		// 管理界面目录
		└── reading		// 读书界面目录
		    ├── account
		    └── index.html	// 阅读首页目录

