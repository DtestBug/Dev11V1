def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'user_id': user.id,  # 数据库内的id
        'user_name': user.username,  # 数据库内的name
        'token': token  # jwt加密方法生成的token
    }