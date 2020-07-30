from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict
# Create your views here.
from .models import Projects
import json
import time

class index_page(View):

    def get(self,request):
        res = {'dicts':[]}
        lists = Projects.objects.all()
        for i in lists:
            dicts = model_to_dict(i)
            dicts['create_time'] = i.create_time.strftime('%Y-%m-%d %H:%M:%S')
            dicts['upd'] = i.upd.strftime('%Y-%m-%d %H:%M:%S')
            res['dicts'].append(dicts)
        return JsonResponse(res,json_dumps_params={"ensure_ascii": False})

    # def get(self,request,pk=None):
    #     pro_obj = Projects.objects.get(id=pk)
    #     data = model_to_dict(pro_obj)
    #     data['create_time'] = pro_obj.create_time.strftime('%Y-%m-%d %H:%M:%S')
    #     data['upd'] = pro_obj.upd.strftime('%Y-%m-%d %H:%M:%S')
    #     return JsonResponse(data,json_dumps_params={"ensure_ascii": False})

    def post(self,request):
        Cr_data = json.loads(request.body)#将数据转换为字典格式,获取请求之后发送的json数据
        res = {}
        Projects.objects.create(**Cr_data)#**Cr_data传入多条数据，post上传的数据创建到数据库
        res['msg'] = '创建成功'
        res['code'] = 0
        return JsonResponse(res)

    def put(self,request,pk=None):
        Cr_data = json.loads(request.body)#将数据转换为字典格式,获取请求之后发送的json数据
        res = {}
        Projects.objects.filter(id=pk).update(**Cr_data)
        res['msg'] = '更新成功'
        res['code'] = 0
        return JsonResponse(res, json_dumps_params={"ensure_ascii": False})

    def delete(self,request,pk=None):
        Projects.objects.get(id=pk).delete()
        res = {}
        res['msg'] = '删除数据!'
        res['code'] = 0
        return JsonResponse(res, json_dumps_params={"ensure_ascii": False})












