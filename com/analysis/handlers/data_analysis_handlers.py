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
from com.analysis.tasks.data_analysis import *


class SingleFactorVarianceAnalysis(BaseAnalysisRequest):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):

        response = yield self.celery_task(single_factor_variance_analysis.apply_async, params=args)
        print response.result
        self.write(response.result[2])

    def post(self, *args, **kwargs):
        pass


class ChiSquareTest(BaseAnalysisRequest):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        response = yield self.celery_task(chi_square_test.apply_async, params=args)
        print(response.result)
        self.write(response.result)

    def post(self, *args, **kwargs):
        pass


class Frequency(BaseAnalysisRequest):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        response = yield self.celery_task(frequency.apply_async, params=args)
        self.write(response.result[1])

    def post(self, *args, **kwargs):
        pass


class MeanValue(BaseAnalysisRequest):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        response = yield self.celery_task(mean_value.apply_async, params=args)
        self.write(response.result[1])

    def post(self, *args, **kwargs):
        pass


class CrossTable(BaseAnalysisRequest):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        response = yield self.celery_task(cross_table.apply_async, params=args)
        self.write(response.result[1])

    def post(self, *args, **kwargs):
        pass


class DataPivotTable(BaseAnalysisRequest):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        response = yield self.celery_task(data_pivot_table.apply_async, params=args)
        self.write("ok")

    def post(self, *args, **kwargs):
        pass


class CorrelationAnalysis(BaseAnalysisRequest):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        response = yield self.celery_task(correlation_analysis.apply_async, params=args)
        self.write(response.result)

    def post(self, *args, **kwargs):
        pass


class GeneralLinearRegressionAnalysis(BaseAnalysisRequest):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        response = yield self.celery_task(general_linear_regression_analysis.apply_async, params=args)
        self.write(response.result)

    def post(self, *args, **kwargs):
        pass
