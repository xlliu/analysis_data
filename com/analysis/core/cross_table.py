#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: cross_table.py
@time: 2016/8/23 18:01
"""
import pandas as pd
import numpy as np
from com.analysis.core.base import Base
from com.analysis.utils.err import ErrorCode


class CT(Base):

    def do_(self, *args):
        def perConvert(ser):
            return ser / float(ser[-1])
        column_list, result = self.get_result(*args)
        ct = pd.crosstab(result[column_list[0]], result[column_list[1]], margins=True).apply(perConvert, axis=1)
        return ErrorCode.SUCCESS, self.generator_view(ct)
