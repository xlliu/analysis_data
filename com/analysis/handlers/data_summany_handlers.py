#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: data_analysis_handlers.py
@time: 2016/8/18 11:16
"""
import tornado.gen
from com.analysis.core.base import BaseAnalysisRequest
from com.analysis.tasks.data_analysis import value_summany

class ValueSummany(BaseAnalysisRequest):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        response = yield self.celery_task(value_summany.apply_async, params=args)
        self.write(response.result[1])

    def post(self, *args, **kwargs):
        pass
