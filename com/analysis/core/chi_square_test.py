#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: chi_square_test.py
@time: 2016/8/23 15:33
"""
from StringIO import StringIO

from com.analysis.core.base import Base
from scipy.stats import chisquare
# from pyvttbl import DataFrame


class CST(Base):

    def do_(self, *args):
        # 'value', 'group'
        column_list, result = self.get_result(*args)
        result_data =  chisquare(result[column_list[0]], result[column_list[1]])
        print result_data
        msg = "x2: %s, P_value: %s" % tuple(result_data)
        return msg
