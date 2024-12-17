# -*- coding: utf-8 -*-

# from src.handler import ShooterHandler
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self):
        self.write("This is Tornado")
