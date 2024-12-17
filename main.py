# -*- coding: utf-8 -*-
__author__ = 'lehman'

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import logging
from src.logconfig import setup_logging
from src.route import application_route
from config import port

tornado.options.define("port", default=port, type=int, help="run server on the given port")
app = tornado.web.Application(
    handlers=application_route,
    debug=True,
)

http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(tornado.options.options.port)
setup_logging()
logging.info(f"Starting Tornado server on http://127.0.0.1:{port}")
tornado.ioloop.IOLoop.current().start()
# tornado.ioloop.IOLoop.instance().start()

