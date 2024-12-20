# -*- coding: utf-8 -*-

from src.handler.index import IndexHandler
from src.handler import LoginHandler
from src.handler.userHandler import UserAdd, UserModify, UserDelete, UserGet
from src.handler.cdnHandler import RefreshAliyunCdn, RefreshCloudFlareCdn, GetRefreshAliyunHistory, \
    GetRefreshCloudFlareHistory

application_route = [
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/user/add", UserAdd),
    (r"/user/modify", UserModify),
    (r"/user/delete", UserDelete),
    (r"/user/getcurrent", UserGet),
    (r"/refresh/aliyun", RefreshAliyunCdn),
    (r"/refresh/cloudflare", RefreshCloudFlareCdn),
    (r"/refresh/record/aliyun", GetRefreshAliyunHistory),
    (r"/refresh/record/cloudflare", GetRefreshCloudFlareHistory),

]
