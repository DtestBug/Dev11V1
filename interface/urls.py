from django.contrib import admin
from django.urls import path
from interface.views import Interface,Interfaces

urlpatterns = [
    path('interface/<int:pk>', Interface.as_view()), # GET接口-查询指定数据
    path('interface/', Interface.as_view()),

    path('interfaces/', Interfaces.as_view()), # get查询所有数据
]




