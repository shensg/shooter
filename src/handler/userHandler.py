# -*- coding: utf-8 -*-

from datetime import datetime
from src.handler import BaseHandler
from src.models.sys import User
from src.utils import base64_encode
from config import data_code
from src.handler import login_jwt_required


class UserAdd(BaseHandler):
    @login_jwt_required
    def post(self):
        user_data = User.select().where(User.name == self.get_json_body("username")).get()
        try:
            if user_data.name:
                print("User already existence!!!")
                data_code["code"] = 208
                data_code["msg"] = "User already existence"
                self.write(data_code)
            else:
                User.insert(name=self.get_json_body("username"), nickname=self.get_json_body("nickname"),
                            email=self.get_json_body("email"), password=base64_encode(self.get_json_body("password")),
                            title_url=self.get_json_body("titleUrl"), describe=self.get_json_body("describe"),
                            u_group_id=self.get_json_body("uGroupId"), create_at=datetime.now())
                data_code["msg"] = "User add success"
                self.write(data_code)
        except EOFError as e:
            print("Add user error: ", e)
            data_code["msg"] = e
            self.write(data_code)


class UserModify(BaseHandler):
    @login_jwt_required
    def post(self):
        try:
            User.update(nickname=self.get_json_body("nickname"), email=self.get_json_body("email"),
                        title_url=self.get_json_body("titleUrl"), describe=self.get_json_body("describe"),
                        update_at=datetime.now()).where(User.user_id == self.get_json_body("userId")).execute()
            data_code["msg"] = "User modify success"
            self.write(data_code)
        except EOFError as e:
            print("Modify user error: ", e)
            data_code["msg"] = e
            self.write(data_code)


class UserDelete(BaseHandler):
    @login_jwt_required
    def post(self):
        User.delete().where(User.user_id == self.get_json_body("userId"))
        data_code["msg"] = "User delete success"
        self.write(data_code)


class UserGet(BaseHandler):
    @login_jwt_required
    def get(self):
        try:
            user_data = User.select().where(User.name == self.get_query_param("username")).get()
            result = {"userId": user_data.user_id, "username": user_data.name, "nickname": user_data.nickname,
                      "email": user_data.email, "titleUrl": user_data.title_url, "describe": user_data.describe}
            data_code["data"] = result
            data_code["msg"] = "Get user information success"
            self.write(data_code)
        except EOFError as e:
            print("Get user information error: ", e)
            data_code["msg"] = e
            self.write(data_code)
