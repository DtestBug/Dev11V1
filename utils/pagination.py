from rest_framework.pagination import PageNumberPagination


class Mypagination(PageNumberPagination):
    page_size = 1  # 默认每页1条数据
    page_query_param = 'p'  # 查询字符串的key值 p=2

    page_size_query_param = 's' #
    max_page_size = 50  # 最多每一页显示50条

