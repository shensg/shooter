# JWT 配置
SECRET_KEY = ""  # 替换为实际的密钥(任意生成的一段随机数，建议16-32位)
ALGORITHM = "HS256"  # 加密算法
EXPIRATION_TIME = 60  # Token 过期时间（分钟）

# app port
port = 8000

db_config = {
    "database": "shooter",
    "user": "root",
    "password": "shooter",
    "host": "mysql",
    "port": 3306,
    "charset": "utf8"
}

data_code = {
    "code": 200,
    "data": "",
    "msg": ""
}