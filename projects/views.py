from .models import Project_Mo
from .serializers import ProjectModelSerializer, ProjectsNamesModelSerializer,InterFacesByProjectIdModelSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from utils.pagination import Mypagination
import logging
from rest_framework import permissions  # 认证

logger = logging.getLogger("test")  # 日志器为settings.py中定义的日志器名


class XXXMinxin:
    def list(self, *args, **kwargs):
        lists = self.filter_queryset(self.get_queryset())  # 覆盖重写查询集lists
        page = self.paginate_queryset(lists)
        if page is not None:
            serializer_obj = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer_obj.data)
        one = self.get_serializer(instance=lists, many=True)
        return Response(one.data,status=status.HTTP_200_OK)  # 1.status指定响应状态码


class Projects(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Project_Mo.objects.all() # 查询集
    serializer_class = ProjectModelSerializer # 序列化器类
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # 过滤引擎,排序引擎
    filterset_fields = ['name', 'leader', 'id']  #过滤字段
    ordering_fields = ['id', 'name']  # 排序引擎   示例：http://127.0.0.1:8000/index/projects/?ordering=id，id前面加-可以倒序
    pagination_class = Mypagination  # 在视图中指定分页

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Project(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Project_Mo.objects.all()  # 查询集
    serializer_class = ProjectModelSerializer  # 序列化器类

    # 查询数据库所有数据
    def get(self,request,  *args, **kwargs):
        return self.retrieve(request,  *args, **kwargs)
        # 过滤需要安装第三方模块django-filter，还有再设置内的子应用注册django_filters,
        # 再导入过滤引擎：from django_filters.rest_framework import DjangoFilterBackend
        # pip install django - filter

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# viewsets.ModelViewSet支持以上所有功能（查，建，改，删）
class ProjectsViewSet(viewsets.ModelViewSet):  # 支持对列表数据进行过滤，排序，分页操作

    # 以下内容均为接口文档内的操作描述
    """
    项目视图
    list:
        获取项目的列表信息
    create:
        创建新的项目
    names:
        查看项目名字
    read:
        读取项目详情
    update:
        更新数据
    partial_update:
        局部更新
    delete:
        删除数据
    interfaces:
        interfaces项目数据
    """

    queryset = Project_Mo.objects.all()  # 查询集
    serializer_class = ProjectModelSerializer  # 序列化器类，ProjectsNamesModelSerializer、ProjectModelSerializer
    pagination_class = Mypagination  # 在视图中指定分页
    # authentication_classes = ['']  # authentication_classes在视图中指定权限，可以在列表中添加多个权限类
    permission_classes = [permissions.IsAuthenticated]  # 视图中指定的权限优先级大于全局指定的权限

    # 可以试用action装饰器去自定义动作方法
    # methods参数默认为['get']，可以定义支持请求方式['get', 'post', 'put']
    # detail参数为必传参数，指定是否为详情数据（如果需要传递主键ID，那么detail=True,否则为False）
    # 添加url_path指定url路径，不添加则默认为action名称(当前为names)
    # url_name指定url的名称，默认为action名称(当前names)
    @action(methods=['get'], detail=False)  # methods请求方式。  detail=True是详情数据，=False的时候是列表类型的数据# url_path='nnn'
    def names(self, request):
        serializer_obj = self.get_serializer(instance=self.get_queryset(), many=True)
        data = serializer_obj.data
        logger.debug(data)  # 定义日志器用于记录日志，logging.getLogging('全局配置settings.py中定义的日志器名')
        # 进行过滤和分页功能
        # serializer_obj = Mypagination
        return Response(data)

    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_obj = self.get_serializer(instance=instance)
        return Response(serializer_obj.data)

    def get_serializer_class(self):
        if self.action == 'names':
            return ProjectsNamesModelSerializer

        elif self.action == 'interfaces':
            return InterFacesByProjectIdModelSerializer

        else:
            return self.serializer_class








