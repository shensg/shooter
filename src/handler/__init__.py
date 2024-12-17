import tornado.web
import jwt
import datetime
import logging
from functools import wraps
from src import BaseHandler
from config import SECRET_KEY, ALGORITHM, EXPIRATION_TIME
from src.models.sys import User
from src.utils import base64_decode

# 配置日志
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def jwt_required(handler_method):
    """JWT 认证装饰器"""
    @wraps(handler_method)
    def wrapper(self, *args, **kwargs):
        auth_header = self.request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            self.set_status(401)
            self.write({"error": "Authorization header missing or invalid"})
            return

        token = auth_header.split(" ")[1]  # 提取 Token
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            self.current_user = payload.get("sub")  # 从 Token 中获取用户信息
        except jwt.ExpiredSignatureError:
            self.set_status(401)
            self.write({"error": "Token has expired"})
            return
        except jwt.InvalidTokenError:
            self.set_status(401)
            self.write({"error": "Invalid token"})
            return

        return handler_method(self, *args, **kwargs)

    return wrapper

class LoginHandler(BaseHandler):
    """登录接口"""
    def post(self):
        # 获取登录信息
        username = self.get_json_body("username")
        password = self.get_json_body("password")

        # 验证用户名和密码
        user_data = User.select().where(User.name == username).get()
        passwd_decode = base64_decode(user_data.password)
        if username in user_data.name and passwd_decode == password:
            # 生成 JWT Token
            expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPIRATION_TIME)
            payload = {
                "sub": username,  # 用户名
                "exp": expiration,  # 过期时间
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
            logging.info(f"User '{username}' logged in successfully.")
            self.write({"token": token})  # 返回 Token
        else:
            print(user_data.name, user_data.password)
            self.set_status(401)
            logging.warning(f"Failed login attempt for username: {username}")
            self.write({"error": "Invalid username or password"})
