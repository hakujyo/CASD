# CASD
code autogen system based on django

# 工程信息
1. 初始化项目
```
django-admin startproject mysite
```

2. 初始化app
```
python manage.py startapp polls
```
在settings.py中注册INSTALLED_APPS

# 管理界面
创建管理界面
```
python manage.py createsuperuser
```
url：
http://127.0.0.1:8000/admin/login/?next=/admin/

必须提供的信息：
- admin.py（向管理页面中加入应用，包括应用下的models）


# model
通过migrate命令，根据models.py自动创建sql语句，维护数据库

必须提供的信息：
- models.py
- settings.py中数据库引擎信息，比如 ENGINE 、 USER 、 PASSWORD 、 HOST 等等

# api
每个api对应修改几个地方：
1. 路由

需要设置的配置项：
- setting.py中的ROOT_URLCONF 
- 新app中的url需要在project级别的urls.py里注册
- app层级的url.py

2. 实际增删改查操作
- 对应的数据库操作，需要提供：
  - 增：数据库名，表名
  - 删：数据库名，表名，删分通过id删除和先查询再删除
  - 改：数据库名，表名，具体的filter字段，需要更改的内容
  - 查：数据库名，表名，具体的filter字段
- 返回体可能有很多种类型，生成对应的jsonresponse等等

主要是具体需要修改views.py的部分，一个api生成一个views文件。

3. 报错信息


# templates
前后端分离，不考虑

# 单测

# 具体实现
输入：json文档

输出：py文件

为每个小功能提供模版代码，叠加的方式生成整个代码块。
如：
```
{
    "api": "polls/<int:question_id>/",
    "method": "GET",
    "responseType": "application/json;charset=utf-8",
    "operation": {
        "op": 1,
        "method": "GETSQL",
        "model": "Question",
        ”find“: "question_text"
    }  
}
```
对应生成的views：
```
from django.http.response import HttpResponse
import json

from polls.models import Question

def GET(request):
    if request.method == 'GET':
        result = {
            "status": "ok",
            "body": {},
            "message": ""
        }
        question_id = request.GET.get('question_id')
        q = Question.objects.get(pk=1)
        result["body"]["question_text"] = q.question_text
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
   else:
        result = {
            "status": "error",
            "body": {},
            "message": "Wrong method!"
        }
        return HttpResponse(result,content_type='application/json;charset=utf-8')
```
为保证py文件生成的速度以及不被覆盖，每个文件尽可能独立, 即一个api生成一个views文件。
