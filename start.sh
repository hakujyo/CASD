#!/bin/bash
#初始化python环境，可容器化
source venv/bin/activate
#初始化项目
django-admin startproject mysite
#初始化app
python manage.py startapp polls



python manage.py runserver 8080
