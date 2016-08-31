#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: defaulthandler.py
@time: 2016/8/5 14:12
"""
import json

import tornado.gen
import tornado.web
from tornado.httpclient import AsyncHTTPClient
from tornado.web import RequestHandler

from com.analysis.tasks.data_analysis import *


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")


class SleepHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.sleep(12)
        self.write("when i sleep 65s")
        # self.finish()
        # time.sleep(10)
        # self.write("when i sleep 5s")


class GenAsyncHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://www.baidu.com")
        if response.code == 200:
            # resp = escape.xhtml_escape(response.body)
            self.write(json.dumps(response.body, indent=4, separators=(',', ':')))
            # self.render(json.dumps(resp, indent=4, separators=(',', ':')))


class Users(RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        """
        :param: TASK
        :param: QUEUE
        :param: CALLBACK

        :return: RESPONSE
        """
        # celery.send_task("query_users", args=["shi is args"], queue="default_analysis",
        #                             callback=self.on_success)
        # def on_success(self, response):
        #     self.write(response.result)
        #     self.finish()
        response = yield tornado.gen.Task(query_users.apply_async, args=["shi is args"], queue="default_analysis")
        self.write(response.result)



class JustNowHandler(RequestHandler):
    def get(self):
        self.write("i hope just now see you")

