from django.urls import path
from projects import views
from rest_framework.routers import DefaultRouter,SimpleRouter

# 第一步：创建一个路由对象
# router = SimpleRouter()
# DefaultRouter相比SimpleRouter，自动添加了一条路径的路由/》可浏览的api页面
router = DefaultRouter()  # 默认路由，(根路径)

# 使用路由对象.register()方法进行注册
# 第一个参数指定路由前缀，r'子应用名小写'
# 第二个参数指定视图集views.py中的类，不需要调用as_view
router.register(r'projects', views.ProjectsViewSet)  # 注册路由

urlpatterns = [
]

# 第二步：使用路由对象.urls属性来获取自动生成的路由条目，需要将这个列表添加至urlpatterns
# 添加路由条目
urlpatterns += router.urls