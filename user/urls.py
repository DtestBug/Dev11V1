from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token  # 登录类视图



urlpatterns = [

    path('login/', obtain_jwt_token),
]
