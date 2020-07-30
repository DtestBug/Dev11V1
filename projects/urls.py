from django.contrib import admin
from django.urls import path
from projects.views import index_page

urlpatterns = [
    path('projects/<int:pk>', index_page.as_view()),#GET接口-查询指定数据
    path('projects/', index_page.as_view()),#GET接口-查询所有数据
]
