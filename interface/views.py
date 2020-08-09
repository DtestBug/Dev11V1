from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Interface_Mo
import json
from .serializers import InterfaceSerializer,InterfaceModelSerializer


ret1 = {
    'msg': '数据不存在',
    'code': 10001,
}

ret2 = {
    'msg': '参数有误',
    'code': 10002,
}

ret3 = {'msg': '操作成功',
        'code': 10003,
        }

class Interface(View):

    # b. instance参数可以传查询集（多条记录），加上many=True
    # d.如果未传递many=True参数，那么序列化器对象.data返回的是字典，否则返回一个嵌套字典的列表

    def get(self, request, pk):
        try:
            pro_obj = Interface_Mo.objects.get(id=pk)
        except Exception as e:
            return JsonResponse(ret1, json_dumps_params={"ensure_ascii": False}, )

        one = InterfaceModelSerializer(
            instance=pro_obj)  # 查询单个数据的时候不能加many=True否则报错:TypeError: 'Project_Mo' object is not iterable
        return JsonResponse(one.data, json_dumps_params={"ensure_ascii": False}, safe=False)

    def post(self, request):

        Cr_data = json.loads(request.body)  # 将数据转换为字典格式,获取请求之后发送的json数据
        res = InterfaceModelSerializer(data=Cr_data)
        try:
            res.is_valid(raise_exception=True)
        except Exception as e:
            ret2.update(res.errors)
            return JsonResponse(ret2, status=400)
        res.save()  # 使用序列化器对象.save()可以自动调用序列化器类中的create方法
        return JsonResponse(res.data, status=201)

    def put(self, request, pk):
        try:
            pro_obj = Interface_Mo.objects.get(id=pk)
        except Exception as e:
            return JsonResponse(ret1, json_dumps_params={"ensure_ascii": False})
        Cr_data = json.loads(request.body)  # 将数据转换为字典格式,获取请求之后发送的json数据
        res = InterfaceModelSerializer(instance=pro_obj,
                                     data=Cr_data)  # instance传递的参数为查询出来的参数，data传递的参数为需要更新的参数,必须用sava来保存
        try:
            res.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(res.errors, status=400)
        res.save()  # save方法自动调用update
        return JsonResponse(res.data, status=201)

    def delete(self, request, pk):
        try:
            pro_obj = Interface_Mo.objects.get(id=pk)
        except Exception as e:
            return JsonResponse(ret1, json_dumps_params={"ensure_ascii": False}, )
        pro_obj.delete()
        ret1['data'] = f'id:{pk}'
        return JsonResponse(ret3)

class Interfaces(View):

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
        lists = Interface_Mo.objects.all()
        one = InterfaceModelSerializer(instance=lists, many=True)
        return JsonResponse(one.data, json_dumps_params={"ensure_ascii": False}, safe=False)