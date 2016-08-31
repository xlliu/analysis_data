#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: mean_value.py
@time: 2016/8/23 12:21
"""
from com.analysis.core.base import Base
from com.analysis.utils.err import ErrorCode


class MV(Base):

    def do_(self, *args):
        column_list, result = self.get_result(*args)
        data = result.describe()
        return ErrorCode.SUCCESS, self.generator_view(data)
