# -*- coding: utf-8 -*-

from src.handler.index import IndexHandler
from src.handler import LoginHandler
from src.handler.userHandler import UserAdd, UserModify, UserDelete, UserGet
from src.handler.cdnHandler import RefreshAliyunCdn, RefreshCloudFlareCdn, GetRefreshHistoryRecord
from src.handler.pathHandler import PathAdd, PathModify, PathDelete, PathGet

application_route = [
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/user/add", UserAdd),
    (r"/user/modify", UserModify),
    (r"/user/delete", UserDelete),
    (r"/user/getcurrent", UserGet),
    (r"/refresh/aliyun", RefreshAliyunCdn),
    (r"/refresh/cloudflare", RefreshCloudFlareCdn),
    (r"/refresh/record/get", GetRefreshHistoryRecord),
    (r"/path/get", PathGet),
    (r"/path/delete", PathDelete),
    (r"/path/modify", PathModify),
    (r"/path/add", PathAdd),

]
