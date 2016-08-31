#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: frequency.py
@time: 2016/8/23 11:27
"""
import pandas as pd

from com.analysis.core.base import Base
from com.analysis.utils.err import ErrorCode


class Frequency(Base):

    def do_(self, *args):
        column_list, result = self.get_result(*args)
        rd = pd.DataFrame(result[cl].value_counts() for cl in column_list)
        return ErrorCode.SUCCESS, self.generator_view(rd)
