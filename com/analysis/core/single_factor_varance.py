#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: single_factor_varance.py
@time: 2016/8/22 18:56
"""
from pygal.style import LightStyle
import pygal
from scipy.stats import levene
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols

from com.analysis.core.base import Base
from com.analysis.utils.err import ErrorCode


class SFV(Base):

    def do_(self, *args):
        """
            eg:
                line_chart = pygal.Bar()
                line_chart.title = 'Browser usage evolution (in %)'
                line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
                line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
                line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
                line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
                line_chart.value_formatter = lambda x: '%.2f%%' % x if x is not None else '∅'
                line_chart.render_table(style=True, total=True)
            :param args:
            :return:
            """

        column_list, result = self.get_result(*args)
        W, pval = levene(result[column_list[0]], result[column_list[1]])
        massage = "W: %s, p-value: %s" % (W, pval)
        print(massage)
        anova_results = anova_lm(ols('%s~C(%s)' % (column_list[1], column_list[0]), result).fit())
        view = self.generator_view(anova_results)

        return ErrorCode.SUCCESS, massage, view
