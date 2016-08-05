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
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")
