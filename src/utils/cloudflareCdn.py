# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.

from requests import post
from src.models.sys import Secrets


class CfRefresh(object):
    def __init__(self, **kwargs):
        self.host_list = kwargs['data']['data']
        self.hosts = self.host_list[0].split('/')[2]

    def refresh(self):
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
        return r
