# -*- coding: utf-8 -*-

import ast
from datetime import datetime
from config import data_code
from src.handler import BaseHandler
from src.utils.cdn_refresh import CfRefresh, AliyunRefresh, return_hostname
from src.models.sys import Secrets
from src.models.refresh_cdn import RefreshHistory


class RefreshAliyunCdn(BaseHandler):
    def post(self):
        data = self.get_json_body('data')
        host_list = data['data']['data']
        hosts = host_list[0].split('/')[2]
        hostname = return_hostname(hosts)
        s_data = Secrets.select().where(Secrets.name == hostname).get()
        aliyun = AliyunRefresh(host_list, s_data.access_key_id, s_data.access_key_secret)
        r = aliyun.refresh()
        if r['success']:
            RefreshHistory.insert(platform="aliyun", refresh_url=host_list, created_at=datetime.now()).execute()
        else:
            RefreshHistory.insert(platform="aliyun", refresh_url=host_list, stated=2,
                                  created_at=datetime.now()).execute()
        self.write(data_code)


class RefreshCloudFlareCdn(BaseHandler):
    def post(self):
        data = self.get_json_body('data')
        host_list = data['data']['data']
        hosts = host_list[0].split('/')[2]
        hostname = return_hostname(hosts)
        s_data = Secrets.select().where(Secrets.name == hostname).get()
        cf = CfRefresh(host_list)
        r = cf.cf_refresh(s_data.zone_id, s_data.access_key_secret)
        if r['success']:
            RefreshHistory.insert(platform="cloudflare", refresh_url=host_list, created_at=datetime.now()).execute()
        else:
            RefreshHistory.insert(platform="cloudflare", refresh_url=host_list, stated=2,
                                  created_at=datetime.now()).execute()
        self.write(data_code)


class GetRefreshHistoryRecord(BaseHandler):
    def get(self):
        platform = self.get_query_param('platform')
        last_record = RefreshHistory.select().where(RefreshHistory.platform == platform).order_by(
            RefreshHistory.created_at.desc()).limit(1).get()
        data = {
            'stated': last_record.stated,
            "createAt": f"{last_record.created_at}",
            "record": ast.literal_eval(last_record.refresh_url)
        }
        data_code['data'] = data
        self.write(data_code)
