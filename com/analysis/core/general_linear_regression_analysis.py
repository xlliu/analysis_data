#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: general_linear_regression_analysis.py
@time: 2016/8/24 10:02
"""

import statsmodels.api as sm
from patsy.highlevel import dmatrices

from com.analysis.core.base import Base


class GLRA(Base):

    def do_(self, *args):

        column_list, result = self.get_result(*args)
        y, X = dmatrices('%s ~ %s' % tuple(column_list), data=result, return_type='dataframe')
        mod = sm.OLS(y, X)
        res = mod.fit()
        return res.summary().as_html()
