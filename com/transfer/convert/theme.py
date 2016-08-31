#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: ??
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: extry.py
@time: 2016/7/27 14:37
"""
import pandas as pd
from com.transfer.convert.common import BaseDBObject
from com.transfer.utils.err import ErrorCode

class Theme(BaseDBObject):

    def __init__(self, filename):
        super(Theme, self).__init__()
        self.filename = filename
        self.__excel2db()

    def __excel2db(self):
        try:
            print("-"*30)
            rel = pd.read_excel(self.filename)
            print("="*30)
            rel.to_sql(
                "data_theme", con=self._stata_engine_data_index, if_exists="append",
                chunksize = 3000 
            )
            print("+"*30)
            
        except Exception as e:
            print(e)
        finally:
            self.session.close()
        return ErrorCode.SUCCESS
