from django.db import models
# Create your models here.

# 一个mysql软件中，可以有多个数据库
# 一个数据库中可以有多张数据表
# 一个数据表中，有多条数据（多条记录）以及多个字段（多个列）

# 1.可以在子应用project/models.py文件中，来定义数据模型
# 2.一个数据模型类对应一个数据表
# 3.数据模型类，需要继承model父类或者model子类
# 4.在数据模型类中，添加的类属性（field对象）来对应数据表中的字段
# 5.创建完数据库模型类之后，需要迁移才能生成数据表
# 6.会自动创建字段名为id的类属性，自增，主键，非空
# a.生成迁移脚本，放在project/migrations目录中：python manage.py makemigrations
# b.执行迁移脚本：python manage.py mirgrate
# c.只需要迁移其中一个子应用的话可以在命令后加子应用目录名称
# 例：python manage.py makemigrations project
# 确认命令之后提示：No changes detected in app 'project'
# 说明这个目录已经迁移过了，并且没有改动
# sqlmigrate 的用法需要加上子应用名称空格之后再加上迁移脚本：0001_initial
# python manage.py sqlmigrate project 0001_initial
# 会自动创建一个主键ID
# 变更已有数据库信息顺序，先执行：
# 1.python manage.py makemigrations project（为子应用名）
# 2.python manage.py migrate project(子应用名)
# 3.查看数据库已变更的信息
class Project_Mo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='项目名称', help_text='项目名称',
                            unique=True)
    leader = models.CharField(max_length=50, verbose_name='项目负责人', help_text='项目负责人')
    tester = models.CharField(max_length=50, verbose_name='测试人员', help_text='测试人员')
    programmer = models.CharField(max_length=50, verbose_name='开发人员', help_text='开发人员')
    desc = models.TextField(verbose_name='项目简介', help_text='项目简介', blank=True, default='XXX简介', null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间', )
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')


    class Meta:
        db_table = 't_Django_projects'
        verbose_name = '项目表'

    def __str__(self):
        return f'<{self.name}>'



