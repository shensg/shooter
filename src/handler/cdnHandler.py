# -*- coding: utf-8 -*-

from config import data_code
from src.handler import BaseHandler
from src.utils.cloudflareCdn import CfRefresh

class RefreshAliyunCdn(BaseHandler):
    def post(self):
        data = self.get_json_body('data')
        # print(data)
        self.write(data_code)

class RefreshCloudFlareCdn(BaseHandler):
    def post(self):
        data = self.get_json_body('data')
        cf = CfRefresh(data=data)
        r = cf.refresh()
        self.write(data_code)
