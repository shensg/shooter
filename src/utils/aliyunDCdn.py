# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_dcdn20180115.client import Client as dcdn20180115Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dcdn20180115 import models as dcdn_20180115_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from src.models.sys import Secrets


class Sample(object):
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dcdn20180115Client:
        """
        Initialize the Client with the AccessKey of the account
        @return: Client
        @throws Exception
        """
        # The project code leakage may result in the leakage of AccessKey, posing a threat to the security of all resources under the account. The following code examples are for reference only.
        # It is recommended to use the more secure STS credential. For more credentials, please refer to: https://www.alibabacloud.com/help/en/alibaba-cloud-sdk-262060/latest/configure-credentials-378659.
        config = open_api_models.Config(
            # Required, please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID is set.,
            access_key_id=ALIYUN_ACCESS_KEY_ID,
            # Required, please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_SECRET is set.,
            access_key_secret=ALIYUN_ACCESS_KEY_SECRET
        )
        # See https://api.alibabacloud.com/product/dcdn.
        config.endpoint = f'dcdn.aliyuncs.com'
        return dcdn20180115Client(config)

    @staticmethod
    def refresh(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        refresh_dcdn_object_caches_request = dcdn_20180115_models.RefreshDcdnObjectCachesRequest(
            object_path='http://www.aalive.io',
            object_type='Directory'
        #     object_type='File',
        #     object_path='''https://www.aalive.io\
        # https://www.aalive.io/index.html'''
        )
        runtime = util_models.RuntimeOptions()
        try:
            # Copy the code to run, please print the return value of the API by yourself.
            client.refresh_dcdn_object_caches_with_options(refresh_dcdn_object_caches_request, runtime)
        except Exception as error:
            # Only a printing example. Please be careful about exception handling and do not ignore exceptions directly in engineering projects.
            # print error message
            print(error.message)
            # Please click on the link below for diagnosis.
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def refresh_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        refresh_dcdn_object_caches_request = dcdn_20180115_models.RefreshDcdnObjectCachesRequest(
            object_path='http://www.aalive.io',
            object_type='Directory',
            force=True
        )
        runtime = util_models.RuntimeOptions()
        try:
            # Copy the code to run, please print the return value of the API by yourself.
            await client.refresh_dcdn_object_caches_with_options_async(refresh_dcdn_object_caches_request, runtime)
        except Exception as error:
            # Only a printing example. Please be careful about exception handling and do not ignore exceptions directly in engineering projects.
            # print error message
            print(error.message)
            # Please click on the link below for diagnosis.
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


    @staticmethod
    def preload(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        preload_dcdn_object_caches_request = dcdn_20180115_models.PreloadDcdnObjectCachesRequest(
            area='overseas',
            object_path='https://aasgeq.com/'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # Copy the code to run, please print the return value of the API by yourself.
            client.preload_dcdn_object_caches_with_options(preload_dcdn_object_caches_request, runtime)
        except Exception as error:
            # Only a printing example. Please be careful about exception handling and do not ignore exceptions directly in engineering projects.
            # print error message
            print(error.message)
            # Please click on the link below for diagnosis.
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def preload_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        preload_dcdn_object_caches_request = dcdn_20180115_models.PreloadDcdnObjectCachesRequest(
            area='overseas',
            object_path='https://aasgeq.com/'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # Copy the code to run, please print the return value of the API by yourself.
            await client.preload_dcdn_object_caches_with_options_async(preload_dcdn_object_caches_request, runtime)
        except Exception as error:
            # Only a printing example. Please be careful about exception handling and do not ignore exceptions directly in engineering projects.
            # print error message
            print(error.message)
            # Please click on the link below for diagnosis.
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.refresh(sys.argv[1:])

