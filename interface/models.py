from django.db import models
from projects.models import Project_Mo
# Create your models here.
# 表与表之间有哪些关系
# a.一对一:models.OneToOneField
# b.一对多:models.ForeignKey,"一"叫做父表，"多"叫做从表（子表）
# c.多对多:models.ManyToManyField


class Interface_Mo(models.Model):
    # id = models.AutoField(primary_key=True)  # primary=True，True的状态为唯一主键
    name = models.CharField(verbose_name='接口名称', max_length=200,unique=True, help_text='接口名称')
    #1,ForeignKey指定外键字段
    #2,第一个参数为必传参数，为父表模型的引用（模型类名或者使用应用名，父表模型类名）

    #3,第二个参数为必传参数，on_delete,指定父表记录被删除之后，子表中对应记录的处理方式
    #4,models.CASCADE:父表记录被删，子表自动删
    #5,models.SET_NULL,null=True:父表记录被删，子表自动设置为null
    # 如果有ForeignKey外键字段，在views内写数据的时候必须添加有效数据
    projects = models.ForeignKey('projects.Project_Mo', on_delete=models.CASCADE, verbose_name='所属项目',help_text='所属项目')
    tester = models.CharField(verbose_name='测试人员', max_length=50,help_text='测试人员')
    desc = models.CharField(verbose_name='简要描述', max_length=200,null=True,blank=True,help_text='简要描述')

    class Meta:
        db_table = 't_Django_interface'
        verbose_name = '接口信息'
        # 数据库模型类的复数，例：apple->apples
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name