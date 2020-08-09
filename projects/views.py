from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse,Http404
# Create your views here.
from .models import Project_Mo
from .serializers import ProjectSerializer,ProjectModelSerializer
import json

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

ret1 = {
    'msg': '参数有误',
    'code': 10001,
}

ret2 = {'msg': '操作成功',
        'code': 10002,
}

class Project_M(GenericAPIView):

    # b. instance参数可以传查询集（多条记录），加上many=True
    # d.如果未传递many=True参数，那么序列化器对象.data返回的是字典，否则返回一个嵌套字典的列表
    queryset = Project_Mo.objects.all() # 查询集
    serializer_class = ProjectModelSerializer # 序列化器类

    def get_object(self,pk):
        try:
            pro_obj = Project_Mo.objects.get(id=pk)
        except Exception as e:
            raise Http404('哦，我的上帝！您访问的页面飞到九霄云外咯。')
        return pro_obj

    def get(self, request, pk):
        pro_obj = self.get_object(pk)
        one = self.get_serializer(instance=pro_obj)
        return Response(one.data,status=status.HTTP_200_OK)

    def post(self, request):

        Cr_data = json.loads(request.body)  # 将数据转换为字典格式,获取请求之后发送的json数据
        res = self.get_serializer(data=Cr_data)
        try:
            res.is_valid(raise_exception=True)
        except Exception as e:
            ret2.update(res.errors)
            return Response(ret1, status=status.HTTP_400_BAD_REQUEST)
        res.save()  # 使用序列化器对象.save()可以自动调用序列化器类中的create方法
        return Response(res.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        pro_obj = self.get_object(pk)
        res = self.get_serializer(instance=pro_obj, data=request.data)
        try:
            res.is_valid(raise_exception=True)
        except Exception as e:
            ret1.update(res.errors)
            return Response(ret1, status=status.HTTP_400_BAD_REQUEST)
        res.save()  # save方法自动调用update
        return Response(res.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        pro_obj = self.get_object(pk)
        pro_obj.delete()
        ret2['data'] = f'id:{pk}'
        return JsonResponse(ret2)

class Projects_M(GenericAPIView):
    queryset = Project_Mo.objects.all()  # 查询集
    serializer_class = ProjectModelSerializer  # 序列化器类
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # 过滤引擎,排序引擎
    filterset_fields = ['name', 'leader', 'id']  # 过滤字段

    # 在ordering_fields来指定需要排序的字段
    #  前端在过滤时，需要使用ordering作为key,具体的排序字段作为value
    # 默认使用升序过滤，如果要降序，可以在排序字段前使用减号
    ordering_fields = ['id', 'name']  # 排序引擎   示例：http://127.0.0.1:8000/index/projects/?ordering=id，id前面加-可以倒序

    # 查询数据库所有数据
    def get(self, request):
        # JsonResponse转化数据为json格式
        # ProjectModelSerializer：serializers文件内的模型序列化类
        # Projects_Mo.objects.all():查询项目模型里所有的数据
        # instance参数可以传查询集（多条记录），加上many=True
        # 如果未传递many=True参数，那么序列化器对象
        # .data返回的是字典，否则返回一个嵌套字典的列表
        # safe=False：为了允许序列化非dict对象，请将safe参数设置为False
        # json_dumps_params={"ensure_ascii": False}

        lists = self.filter_queryset(self.get_queryset())
        one = self.get_serializer(instance=lists, many=True)
        return Response(one.data, status=status.HTTP_200_OK)








