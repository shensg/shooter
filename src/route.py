# -*- coding: utf-8 -*-

from src.handler.index import IndexHandler
from src.handler import LoginHandler
from src.handler.userHandler import UserAdd, UserModify, UserDelete, UserGet

application_route = [
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/user/add",UserAdd),
    (r"/user/modify",UserModify),
    (r"/user/delete",UserDelete),
    (r"/user/getcurrent",UserGet),

]
