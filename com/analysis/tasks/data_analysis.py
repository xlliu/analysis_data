#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: tasks.py
@time: 2016/8/17 16:37
"""
import time

import pandas as pd
from celery import Celery
from scipy.stats import levene
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

from com.analysis.core.chi_square_test import CST
from com.analysis.core.correlation_analysis import CA
from com.analysis.core.cross_table import CT
from com.analysis.core.data_pivot_table import DPT
from com.analysis.core.frequency import Frequency
from com.analysis.core.general_linear_regression_analysis import GLRA
from com.analysis.core.mean_value import MV
from com.analysis.core.single_factor_varance import SFV
from com.analysis.db.db_engine import DBEngine
from com.analysis.utils.err import ErrorCode
from com.analysis.utils.log import Logger

celery = Celery(
    'com.analysis.tasks.data_analysis',
    broker='amqp://42.62.6.220:5672',
    include='com.analysis.tasks.data_analysis'
)
celery.conf.CELERY_RESULT_BACKEND = "amqp://42.62.6.220:5672"
celery.conf.CELERY_ACCEPT_CONTENT = ['application/json']
celery.conf.CELERY_TASK_SERIALIZER = 'json'
celery.conf.CELERY_RESULT_SERIALIZER = 'json'
celery.conf.BROKER_HEARTBEAT = 30
celery.conf.CELERY_IGNORE_RESULT = False  # this is less important
logger = Logger().getLogger()


@celery.task(name='qu')
def query_users(admin_id):
    # 耗时的数据库操作
    print("=" * 10)
    time.sleep(5)
    print("ssssssssssssssssssssssssssss")
    return "she is db event, %s " % admin_id


@celery.task(name='on_success')
def on_success(response):
    # 获取返回的结果
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
    self.write(response.status)
    self.finish()
    # return response.result
    # self.write(users)
    # self.finish()


@celery.task()
def single_factor_variance_analysis(*args):
    return SFV().do_(*args)


@celery.task()
def chi_square_test(*args):
    return CST().do_(*args)


@celery.task()
def frequency(*args):
    return Frequency().do_(*args)


@celery.task()
def mean_value(*args):
    return MV().do_(*args)


@celery.task()
def cross_table(*args):
    return CT().do_(*args)


@celery.task()
def data_pivot_table(*args):
    return DPT().do_(*args)


@celery.task()
def correlation_analysis(*args):
    return CA().do_(*args)


@celery.task()
def general_linear_regression_analysis(*args):
    return GLRA().do_(*args)


class xlliu_text(object):
    def __init__(self):
        self._stata_engine_default, \
        self._stata_engine_data_index, \
        self._stata_engine_data_base, \
        self._stata_engine_data_options = DBEngine.database_factory(stata=True)

    def test_var(self):
        args = [self.session, "7ebcee81c717cb79535aaa275682e3dc-7ebcee81c717cb79535aaa275682e3dc", "county-neighbcm"]
        # args = [self.session, "7ebcee81c717cb79535aaa275682e3dc", "county-neighbcm"]
        tables = args[1].split("-")
        columon_list = args[2].split("-")

        result = pd.DataFrame(columns=columon_list)
        engine = args[0]
        for table in tables:
            params = [columon_list[0], columon_list[1], table]
            sql = "select %s, %s from %s" % tuple(params)
            result_chunk = pd.read_sql_query(sql, self._stata_engine_data_base)
            result = pd.concat([result, result_chunk])

        W, pval = levene(result[columon_list[0]], result[columon_list[1]])
        print(str(W), str(pval))
        massage = "W: %s, p-value: %s" % (W, pval)
        anova_results = anova_lm(ols('%s~C(%s)' % (columon_list[1], columon_list[0]), result).fit())
        print(anova_results)

        import pygal
        from pygal.style import LightStyle
        # budget = pd.read_csv("mn-budget-detail-2014.csv")
        # budget = budget.sort('amount', ascending=False)[:10]
        # ------------------------------------

        bar_chart = pygal.Bar(style=LightStyle, width=800, height=600,
                              legend_at_bottom=True, human_readable=True,
                              title='')

        #
        # line_chart = pygal.Bar()
        # line_chart.title = 'Browser usage evolution (in %)'
        # line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
        # line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
        # line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        # line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
        # line_chart.value_formatter = lambda x: '%.2f%%' % x if x is not None else '∅'
        # line_chart.render_table(style=True, total=True)

        # --------------------------------------
        bar_chart.x_labels = anova_results.index
        # for index, row in anova_results.iterrows():
        for col in anova_results.columns:
            bar_chart.add(col, anova_results[col])

        # 现在可以渲染到svg和png文件中去了：
        bar_chart.render_table(style=True)

        return ErrorCode, massage, anova_results


if __name__ == '__main__':
    xlliu_text().test_var()
