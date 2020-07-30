from django.contrib import admin
from django.urls import path
from interface.views import index_page

urlpatterns = [
    path('interface/<int:pk>', index_page.as_view()),#GET接口-查询指定数据
    path('interface/', index_page.as_view()),#GET接口-查询所有数据
]
