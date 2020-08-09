from django.contrib import admin
from django.urls import path
from projects.views import Project_M,Projects_M

urlpatterns = [
    path('project/<int:pk>', Project_M.as_view()),#GET接口-查询指定数据
    path('project/', Project_M.as_view()),

    path('projects/', Projects_M.as_view()),
]
