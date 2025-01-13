# -*- coding: utf-8 -*-

from src.handler import BaseHandler
from src.models.sys import Path

class PathAdd(BaseHandler):
    def post(self):
        data = self.get_json_body('data')
        # Path.insert(name = )
