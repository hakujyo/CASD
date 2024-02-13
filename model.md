# MIGRATE
迁移是非常强大的功能，它能让你在开发过程中持续的改变数据库结构而不需要重新删除和创建表 - 它专注于使数据库平滑升级而不会丢失数据。

改变模型需要这三步：

1. 编辑 models.py 文件，改变模型。
2. 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
3. 运行 python manage.py migrate 来应用数据库迁移。

### 命令详解

这个 migrate 命令查看 INSTALLED_APPS 配置， 
并根据 mysite/settings.py 文件中的数据库配置和随应用提供的数据库迁移文件， 创建任何必要的数据库表。

这个 migrate 命令选中所有还没有执行过的迁移（Django 通过在数据库中创建一个特殊的表 django_migrations 来跟踪执行过哪些迁移）并应用在数据库上 - 也就是将你对模型的更改同步到数据库结构上。
> python manage.py migrate

通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 迁移。
> python manage.py makemigrations polls

sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL
> python manage.py sqlmigrate polls 0001

检查项目中的问题，并且在检查过程中不会对数据库进行任何操作
> python manage.py check
