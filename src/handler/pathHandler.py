# -*- coding: utf-8 -*-

from src.handler import BaseHandler
from src.models.sys import Path
from config import data_code


class PathAdd(BaseHandler):
    def post(self):
        data = self.get_json_body('data')
        Path.insert(path=data['path'], describe=data['describe']).execute()
        data_code['msg'] = "Add new path success"
        self.write(data_code)


class PathModify(BaseHandler):
    def post(self):
        data = self.get_json_body('data')
        try:
            Path.update(path=data['path'], describe=data['describe']).where(Path.path_id == data['pid']).execute()
            msg = 'Update path success'
        except RuntimeError as e:
            data_code['code'] = 508
            msg = 'Update path failed, info: ', e
            print(msg)
        data_code['msg'] = msg
        self.write(data_code)


class PathDelete(BaseHandler):
    def post(self):
        data = self.get_json_body('data')
        Path.delete().where(data['pid'])
        data_code['msg'] = 'Delete path success'
        self.write(data_code)


class PathGet(BaseHandler):
    def get(self):
        page = self.get_query_param('page')
        page_size = self.get_query_param('size')
        offset = (page - 1) * page_size
        total = Path.select().count()
        path_data = Path.select().limit(page_size).offset(offset).get()
        data = []
        for path in path_data:
            data.append({"pid": path.path_id, "path": path.path, "describe": path.describe})
        data_code['data'] = {
            "total": total,
            "data": data
        }
        data_code['msg'] = "Get path success"
        self.write(data_code)

