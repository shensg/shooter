# -*- coding: utf-8 -*-
import tornado.web
import json
import logging

# 配置日志
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class BaseHandler(tornado.web.RequestHandler):
    """基础处理器，添加跨域支持"""
    def set_default_headers(self):
        """
        设置默认响应头，允许跨域。
        """
        self.set_header("Access-Control-Allow-Origin", "*")  # 允许所有域名访问
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")  # 允许的 HTTP 方法
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")  # 允许的请求头
        self.set_header("Access-Control-Allow-Credentials", "true")  # 是否允许携带凭证

    def options(self, *args, **kwargs):
        """
        处理 OPTIONS 预检请求。
        """
        self.set_status(204)
        self.finish()

    """基础处理器"""
    def prepare(self):
        """
        初始化请求数据，在请求处理前调用。
        """
        # 提取 GET 请求参数
        self.query_params = {k: self.get_argument(k) for k in self.request.arguments}

        # 提取 POST 请求数据
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            try:
                self.json_body = json.loads(self.request.body)
            except json.JSONDecodeError:
                self.json_body = {}
        else:
            self.json_body = {k: self.get_body_argument(k) for k in self.request.body_arguments}

        logging.info(f"Initialized request data: query_params={self.query_params}, json_body={self.json_body}")

    def write_error(self, status_code, **kwargs):
        """自定义错误响应"""
        self.write({"error": self._reason})
        self.set_status(status_code)

    def get_query_param(self, key, default=None):
        """获取单个查询参数"""
        return self.query_params.get(key, default)

    def get_json_body(self, key, default=None):
        """获取单个 JSON 请求体参数"""
        return self.json_body.get(key, default)

    # def get_json_all_body(self):
    #     """获取单个 JSON 请求体参数"""
    #     return self.json_body

# class DataHandler(BaseHandler):
#     """处理数据的接口"""
#
#     def get(self):
#         """处理 GET 请求"""
#         name = self.get_query_param("name", "Guest")
#         age = self.get_query_param("age", "unknown")
#         self.write({"message": f"Hello, {name}! Your age is {age}."})
#
#     def post(self):
#         """处理 POST 请求"""
#         name = self.get_json_body("name", "Guest")
#         age = self.get_json_body("age", "unknown")
#         self.process_data(name, age)
#
#     def process_data(self, name, age):
#         """处理数据的业务逻辑"""
#         # 在其他方法中使用提取的数据
#         logging.info(f"Processing data for name={name}, age={age}")
#         self.write({"message": f"Data processed for {name}, age {age}."})
