# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List
from alibabacloud_esa20240910.client import Client as ESA20240910Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_esa20240910 import models as esa20240910_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from src.models.sys import Secrets

class Sample(object):
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> ESA20240910Client:
        """
        Initialize the Client with the AccessKey of the account
        @return: Client
        @throws Exception
        """
        # The project code leakage may result in the leakage of AccessKey, posing a threat to the security of all resources under the account. The following code examples are for reference only.
        # It is recommended to use the more secure STS credential. For more credentials, please refer to: https://www.alibabacloud.com/help/en/alibaba-cloud-sdk-262060/latest/configure-credentials-378659.
        config = open_api_models.Config(
            # Required, please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID is set.,
            access_key_id=secret_key_id,
            # Required, please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_SECRET is set.,
            access_key_secret=secret_key_secret
        )
        # See https://api.alibabacloud.com/product/ESA.
        config.endpoint = f'esa.ap-southeast-1.aliyuncs.com'
        return ESA20240910Client(config)

    @staticmethod
    def main(
            args: List[str],
    ) -> None:
        client = Sample.create_client()
        preload_caches_request = esa20240910_models.PreloadCachesRequest(
            site_id=489862422922832,
            content=[
                'https://test.exmaple.com/'
            ]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # Copy the code to run, please print the return value of the API by yourself.
            client.preload_caches_with_options(preload_caches_request, runtime)
        except Exception as error:
            # Only a printing example. Please be careful about exception handling and do not ignore exceptions directly in engineering projects.
            # print error message
            print(error.message)
            # Please click on the link below for diagnosis.
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
            args: List[str],
    ) -> None:
        client = Sample.create_client()
        preload_caches_request = esa20240910_models.PreloadCachesRequest(
            site_id=489862422922832,
            content=[
                'https://test.exmaple.com/'
            ]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # Copy the code to run, please print the return value of the API by yourself.
            await client.preload_caches_with_options_async(preload_caches_request, runtime)
        except Exception as error:
            # Only a printing example. Please be careful about exception handling and do not ignore exceptions directly in engineering projects.
            # print error message
            print(error.message)
            # Please click on the link below for diagnosis.
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
