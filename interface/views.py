from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Interface
import json
from .serializers import ProjectSerializer,ProjectModelSerializer

class index_page(View):

    # def get(self,request):
    #     lists = Interface.objects.all()
    #     one = ProjectSerializer(instance=lists,many=True)
    #     return JsonResponse(one.data,json_dumps_params={"ensure_ascii": False},safe=False)

    # b. instance参数可以传查询集（多条记录），加上many=True
    # d.如果未传递many=True参数，那么序列化器对象.data返回的是字典，否则返回一个嵌套字典的列表
    def get(self,request,pk=None):
        res = {}
        try:
            pro_obj = Interface.objects.get(id=pk)
        except Exception as e:
            res['msg'] = '数据不存在'
            return JsonResponse(res)
        one = ProjectModelSerializer(instance=pro_obj)#查询单个数据的时候不能加many=True否则报错:TypeError: 'Interface' object is not iterable
        return JsonResponse(one.data,json_dumps_params={"ensure_ascii": False},safe=False)

    def post(self,request):
        da = {}
        Cr_data = json.loads(request.body)#将数据转换为字典格式,获取请求之后发送的json数据
        res = ProjectModelSerializer(data=Cr_data)
        try:
            res.is_valid(raise_exception=True)
        except Exception as e:
            da['msg'] = '参数有误'
            da.update(res.errors)
            return JsonResponse(da,status=400, safe=False)
        res.save()
        return JsonResponse(res.data, status=201)

    def put(self,request,pk=None):
        Cr_data = json.loads(request.body)#将数据转换为字典格式,获取请求之后发送的json数据
        res = ProjectModelSerializer(data=Cr_data)
        try:
            res.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(res.errors,status=400)
        obj = Interface.objects.filter(id=pk).update(**res.validated_data)
        ProjectModelSerializer(instance=obj)
        return JsonResponse(res.validated_data, status=201)

    def delete(self,request,pk=None):
        res = {}
        try:
            Interface.objects.get(id=pk).delete()
        except Exception as e:
            res['data'] = f'id:{pk}'
            res['msg'] = '数据不存在'
            res['code'] = 1
            return JsonResponse(res, status=400)
        res['data'] = f'id:{pk}'
        res['msg'] = '删除数据成功!'
        res['code'] = 0
        return JsonResponse(res)