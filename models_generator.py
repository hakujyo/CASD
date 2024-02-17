# /usr/bin/python

import json
import os
import re
import ast, astor, astunparse

modeljson = "mysite/school/models.json"
modelpy = "mysite/school/models.py"
serializerspy = "mysite/school/serializers.py"
# urlfile = "mysite/school/urls.py"
tablename = None
# viewfile = f"mysite/school/{tablename}Views.py"
# getfile = "codetemplates/get.py"
# postfile = "codetemplates/post.py"
# updatefile = "codetemplates/update.py"
# deletefile = "codetemplates/delete.py"
# viewimportfile = "codetemplates/viewimport.py"


def write_models_and_serializers():
    exist = None
    model_content = """"""
    if os.path.exists(modelpy):
        exist = True
    else:
        exist = False
        model_content += """from django.db import models
    \nfrom django.utils import timezone"""

    serializer_exist = None
    serializer_content = """"""
    serializer_create_content = """\n\n    def create(self, validated_data):"""
    serializer_update_content = """\n\n    def update(self, instance, validated_data):"""
    if os.path.exists(serializerspy):
        serializer_exist = True
    else:
        serializer_exist = False
        serializer_content += """from rest_framework import serializers"""

    with open(modeljson, 'r') as inputfile:
        data = json.load(inputfile)
        global tablename
        tablename = data["tableName"].capitalize()
        model_content += """\n\n\nclass %s(models.Model):""" % tablename
        serializer_content += """\nfrom .models import %s
        \n\nclass %sSerializer(serializers.Serializer):\n    id = serializers.IntegerField(read_only=True)""" % (tablename, tablename)
        serializer_create_content += """\n        return %s.objects.create(**validated_data)""" % tablename

        fields = data["fields"]
        for key, info in fields.items():
            if info["type"] == "string":
                max_length = info["max_length"]
                model_content += """\n    %s = models.CharField(max_length=%d)""" % (key, max_length)
                serializer_content += """\n    %s = serializers.CharField(max_length=%d)""" % (key, max_length)
            elif info["type"] == "int":
                model_content += """\n    %s = models.IntegerField()""" % key
                serializer_content += """\n    %s = serializers.IntegerField()""" % key
            serializer_update_content += """\n        instance.%s = validated_data.get('%s')""" % (key, key)

    with open(modelpy, 'a') as modelfile:
        modelfile.write(model_content )

    serializer_update_content += """\n        instance.save()\n        return instance"""
    with open(serializerspy, 'a') as serializersfile:
        serializersfile.write(serializer_content)
        serializersfile.write(serializer_create_content)
        serializersfile.write(serializer_update_content)


def write_views():
    viewfile = f"mysite/school/{tablename}Views.py"
    getfile = "codetemplates/get.py"
    postfile = "codetemplates/post.py"
    updatefile = "codetemplates/update.py"
    deletefile = "codetemplates/delete.py"
    viewimportfile = "codetemplates/viewimport.py"
    with open(viewfile, 'a') as viewfile:
        # print(get)
        with open(viewimportfile, 'r') as viewimportfile:
            file_content = viewimportfile.read().format(tablename=tablename)
            viewfile.write(file_content)
        with open(getfile, 'r') as getfile:
            file_content = getfile.read().format(tablename=tablename)
            viewfile.write("\n" + file_content)
        with open(postfile, 'r') as postfile:
            file_content = postfile.read().format(tablename=tablename)
            viewfile.write("\n\n\n" + file_content)
        with open(updatefile, 'r') as updatefile:
            file_content = updatefile.read().format(tablename=tablename)
            viewfile.write("\n\n\n" + file_content)
        with open(deletefile, 'r') as deletefile:
            file_content = deletefile.read().format(tablename=tablename)
            viewfile.write("\n\n\n" + file_content)

def write_urls():
    urlfile = "mysite/school/urls.py"
    urlcontent = None
    with open(urlfile, 'r') as f:
        urlcontent = f.read()

    root = ast.parse(urlcontent)

    # 创建新的 path 节点
    prefix = tablename.lower()
    new_path_node1 = ast.Expr(
        value=ast.Call(
            func=ast.Name(id='path', ctx=ast.Load()),
            args=[
                ast.Str(s=f'{prefix}/'),
                ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id=f'{tablename}Views', ctx=ast.Load()),
                            attr=f'{tablename}Views',
                            ctx=ast.Load()
                        ),
                        attr='as_view',
                        ctx=ast.Load()
                    ),
                    args=[],
                    keywords=[]
                ),
            ],
            keywords=[
                ast.keyword(arg='name', value=ast.Str(s=f'{prefix}/'))
            ]
        )
    )
    new_path_node2 = ast.Expr(
        value=ast.Call(
            func=ast.Name(id='path', ctx=ast.Load()),
            args=[
                ast.Str(s=f'{prefix}/<int:pk>/'),
                ast.Call(
                    func=ast.Attribute(
                        value=ast.Attribute(
                            value=ast.Name(id=f'{tablename}Views', ctx=ast.Load()),
                            attr=f'{tablename}Views',
                            ctx=ast.Load()
                        ),
                        attr='as_view',
                        ctx=ast.Load()
                    ),
                    args=[],
                    keywords=[]
                ),
            ],
            keywords=[
                ast.keyword(arg='name', value=ast.Str(s=f'{prefix}/'))
            ]
        )
    )

    # 创建新的 path 节点
    prefix = tablename.lower()
    # new_path_node1 = ast.Expr(
    #     value=ast.Call(
    #         func=ast.Name(id='path', ctx=ast.Load()),
    #         args=[ast.Str(s=f'{prefix}/'), ast.Name(id=f'views.{tablename}View.as_view()', ctx=ast.Load()),
    #               ast.Dict(keys="name", values=f'{prefix}')],
    #         keywords=[]
    #     )
    # )
    # new_path_node2 = ast.Expr(
    #     value=ast.Call(
    #         func=ast.Name(id='path', ctx=ast.Load()),
    #         args=[ast.Str(s=f'{prefix}/<int:pk>/'), ast.Name(id=f'views.{tablename}View.as_view()', ctx=ast.Load()),
    #               ast.Dict(keys="name", values=f'{prefix}')],
    #         keywords=[]
    #     )
    # )


    # 找到 urlpatterns 节点
    for node in ast.walk(root):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and \
                node.targets[0].id == 'urlpatterns':
            node.value.elts.append(new_path_node1)
            node.value.elts.append(new_path_node2)

    # 创建 import 节点
    import_node = ast.ImportFrom(module='.', names=[ast.alias(name=f'{tablename}Views', asname=None)], level=0)
    # import_node = ast.Import(names=[ast.alias(name=f'{tablename}Views', asname=None)])
    # import_node = ast.ImportFrom(module='.', names=[ast.alias(name=f'{tablename}View', asname=None)], level=1)

    # 将 import 节点插入到 AST 的开头
    root.body.insert(0, import_node)

    # 将修改后的 AST 转回源代码
    modified_code = astunparse.unparse(root)

    with open(urlfile, 'w') as f:
        f.write(modified_code)
        print(modified_code)


if __name__ == '__main__':
    write_models_and_serializers()
    write_views()
    write_urls()


