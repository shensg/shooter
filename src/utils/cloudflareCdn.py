# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.

import ast
from requests import post
from datetime import datetime
from src.models.sys import Secrets
from src.models.refresh_cdn import RefreshHistory


class CfRefresh(object):
    def __init__(self, **kwargs):
        self.host_list = kwargs['data']['data']
        self.hosts = self.host_list[0].split('/')[2]

    def cf_refresh(self):
        if len(self.hosts.split('.')) >= 3:
            hostname = self.hosts.split('.')[-2]
            hostname += '.'
            hostname += self.hosts.split('.')[-1]
            # print(hostname)
        else:
            hostname = self.hosts
            # print(hostname)
        s_data = Secrets.select().where(Secrets.name == hostname).get()
        token = s_data.access_key_secret
        zone_id = s_data.zone_id
        url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        data = {
            "files": self.host_list
        }
        r = post(url, json=data, headers=headers)
        RefreshHistory.insert(platform="cloudflare", refresh_url=self.host_list, created_at=datetime.now()).execute()
        return r


def get_cf_last_refresh():
    last_record = RefreshHistory.select().where(RefreshHistory.platform == "cloudflare").order_by(
        RefreshHistory.created_at.desc()).limit(1).get()
    data = {
        "createAt": f"{last_record.created_at}",
        "record": ast.literal_eval(last_record.refresh_url)
    }
    return data
