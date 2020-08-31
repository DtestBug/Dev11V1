import jwt
from rest_framework_jwt import views
# 第一部分的header，一般不需要指定，有默认值

# 第二部分，可以指定后端需要存放的一些非敏感的信息
payload = {'username': '小李', 'age': 18}

token = jwt.encode(payload, key='666')  # json web token.jwt加密

one_ver = jwt.decode(token, key='666')  # token解密，key值必须与加密时候的key值一致，否则无法解密会报错
