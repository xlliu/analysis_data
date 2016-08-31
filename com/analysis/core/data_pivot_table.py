#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: data_pivot_table.py
@time: 2016/8/23 17:33
"""
import pandas as pd
import numpy as np

from com.analysis.core.base import Base


class DPT(Base):

    def do_(self, *args):
        # todo 暂时不做，废弃
        column_list, result = self.get_result(*args)
        b = pd.pivot_table(result, index=["xb", "xl"], values=["kf"], aggfunc=[np.mean, len])
        return b
