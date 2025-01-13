# -*- coding: utf-8 -*-

from typing import List
from requests import post
from alibabacloud_dcdn20180115.client import Client as dcdn20180115Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dcdn20180115 import models as dcdn_20180115_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_esa20240910 import models as esa20240910_models
from alibabacloud_esa20240910.client import Client as ESA20240910Client


def return_hostname(hosts):
    if len(hosts.split('.')) >= 3:
        hostname = hosts.split('.')[-2] + '.' + hosts.split('.')[-1]
        # print(hostname)
    else:
        hostname = hosts
        # print(hostname)
    return hostname


class CfRefresh(object):
    def __init__(self, host_list: list):
        self.object_paths = host_list

    def cf_refresh(self, zone_id: str, token: str):
        url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        data = {
            "files": self.object_paths
        }
        response = post(url, json=data, headers=headers)
        return response.json()


class AliyunRefresh(object):
    def __init__(self, host_list: list, access_key_id: str, access_key_secret: str,
                 endpoint: str = 'dcdn.aliyuncs.com'):
        """
        初始化 AliyunRefresh 类并配置 AccessKey 和 Endpoint
        """
        self.object_paths = host_list
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.endpoint = endpoint
        self.client = self.create_client()

    def create_client(self) -> dcdn20180115Client:
        """
        初始化 DCDN 客户端
        :return: DCDN 客户端实例
        """
        config = open_api_models.Config(
            access_key_id=self.access_key_id,
            access_key_secret=self.access_key_secret,
        )
        config.endpoint = self.endpoint
        return dcdn20180115Client(config)

    def determine_object_type(self, object_path: str) -> str:
        """
        判断 object_path 的类型 (File 或 Directory)
        """
        if object_path.endswith('/'):
            return 'Directory'
        else:
            return 'File'

    def refresh(self) -> dict:
        """
        刷新多个 DCDN 缓存路径
        """
        runtime = util_models.RuntimeOptions()

        # for path in self.object_paths:
        object_type = self.determine_object_type(self.object_paths[0])
        path = "\n".join(map(lambda x: str(x), self.object_paths))
        # object_type = self.determine_object_type(path)
        refresh_request = dcdn_20180115_models.RefreshDcdnObjectCachesRequest(
            object_path=path,
            object_type=object_type
        )
        try:
            response = self.client.refresh_dcdn_object_caches_with_options(refresh_request, runtime)
            print(f"刷新成功: {path}, 类型: {object_type}", response)
            return {"success": True, "response": response}
        except Exception as error:
            print(f"刷新失败: {path}, 错误: {error.message}")
            print("推荐解决方案:", error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)
            return {
                "success": False,
                "error_message": error.message,
                "recommendation": error.data.get("Recommend") if error.data else None
            }

    def preload(self, object_path: str, area: str = 'overseas') -> dict:
        """
        预热 DCDN 缓存 :param object_path: 要预热的 URL :param area: 预热区域 ('domestic' 或 'overseas')
        """
        preload_request = dcdn_20180115_models.PreloadDcdnObjectCachesRequest(
            object_path=object_path,
            area=area
        )
        runtime = util_models.RuntimeOptions()
        result = {"success": [], "failure": []}
        try:
            response = self.client.preload_dcdn_object_caches_with_options(preload_request, runtime)
            print("预热成功:", response)
        except Exception as error:
            print("预热失败:", error.message)
            print("推荐解决方案:", error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


class AliyunRefreshEsa:
    def __init__(self, access_key_id: str, access_key_secret: str, endpoint: str = 'esa.ap-southeast-1.aliyuncs.com'):
        """
        初始化 AliyunPreload 类并配置 AccessKey 和 Endpoint
        """
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.endpoint = endpoint
        self.client = self.create_client()

    def create_client(self) -> ESA20240910Client:
        """
        初始化 ESA 客户端
        :return: ESA 客户端实例
        """
        config = open_api_models.Config(
            access_key_id=self.access_key_id,
            access_key_secret=self.access_key_secret,
        )
        config.endpoint = self.endpoint
        return ESA20240910Client(config)

    def refresh(self, site_id: int, content: List[str]) -> dict:
        """
        刷新缓存操作 :param site_id: 站点 ID :param content: 需要预热的 URL 列表 :return: 包含操作结果的字典
        """
        preload_request = esa20240910_models.PreloadCachesRequest(
            site_id=site_id,
            content=content
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = self.client.preload_caches_with_options(preload_request, runtime)
            return {"success": True, "response": response}
        except Exception as error:
            return {
                "success": False,
                "error_message": error.message,
                "recommendation": error.data.get("Recommend") if error.data else None
            }
