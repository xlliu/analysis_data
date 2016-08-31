#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: correlation_analysis.py
@time: 2016/8/23 16:20
"""
from com.analysis.core.base import Base


class CA(Base):

    def do_(self, *args):
        # 相关系数大于0时说明正相关，小于0时负相关。
        column_list, result = self.get_result(*args)
        print("["*100)
        print(result.corr())
        print("]"*100)
        return self.generator_view(result.corr())
