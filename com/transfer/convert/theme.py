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


class MergeTable(BaseDBObject):
    def met(self):
        sql = "select * from data_index_default"
        sql2 = "select * from data_theme"
        dindex = pd.read_sql_query(sql, self._stata_engine_data_index)
        dtheme = pd.read_sql_query(sql2, self._stata_engine_data_index)

        index_theme = pd.merge(dindex, dtheme, how="left", left_on="cid", right_on="cid")
        index_theme.to_sql(
            "data_index_theme", con=self._stata_engine_data_index, chunksize= 3000
        )
	return "ok"


