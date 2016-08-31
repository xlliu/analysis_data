#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: base.py
@time: 2016/8/12 17:34
"""
import pandas as pd
import pygal
import tornado.gen
from pygal.style import LightStyle
from sqlalchemy.orm import sessionmaker
from tornado.web import RequestHandler

from com.analysis.db.db_engine import DBEngine
from com.analysis.utils.log import LogCF


class Base(object):

    @LogCF.open_log(True)
    def __init__(self, **kwargs):
        self.logger = kwargs.get("logger")
        self._stata_engine_default, \
        self._stata_engine_data_index, \
        self._stata_engine_data_base, \
        self._stata_engine_data_options = DBEngine.database_factory(stata=True)

    def get_result(self, *args):
        tables = args[1].split("-")
        column_list = args[2].split("-")
        column_list_param = ",".join(column_list)

        result = pd.DataFrame(columns=column_list)
        engine = self._stata_engine_data_base
        for table in tables:
            # todo 注入漏洞，时间紧先这样
            params = [column_list_param, table]
            sql = "select %s from %s" % tuple(params)
            result_chunk = pd.read_sql_query(sql, engine)
            result = pd.concat([result, result_chunk])
        result_not_nan = result.dropna(axis=0)
        return column_list, result_not_nan

    def generator_view(self, data):

        print(data)
        bar_chart = pygal.Bar(style=LightStyle, width=800, height=600,
                              legend_at_bottom=True, human_readable=True,
                              title='')

        bar_chart.x_labels = data.index.to_series().apply(lambda x: str(x))
        for col in data.columns:
            bar_chart.add(str(col), data[col])

        # 现在可以渲染到svg和png文件中去了：
        # ...
        return bar_chart.render_table(style=True)


class BaseRequest(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseRequest, self).__init__(application, request, **kwargs)


class BaseAnalysisRequest(BaseRequest):
    def __init__(self, application, request, **kwargs):
        super(BaseAnalysisRequest, self).__init__(application, request, **kwargs)
        # self._stata_engine_default, \
        # self._stata_engine_data_index, \
        # self._stata_engine_data_base, \
        # self._stata_engine_data_options = DBEngine.database_factory(stata=True)
        # _DB_session = sessionmaker(bind=self._stata_engine_default)
        # self.session = _DB_session()
        # self._db_list = ["data_base", "data_index", "data_options"]

    @tornado.gen.coroutine
    def celery_task(self, func, params, queue="default_analysis"):
        args_list = list(params)
        args_list.insert(0, "")
        response = yield tornado.gen.Task(func, args=args_list, queue=queue)
        raise tornado.gen.Return(response)
