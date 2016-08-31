#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: stata.py
@time: 2016/7/27 14:40
"""
import time
import uuid

import pandas as pd
from com.transfer.convert.common import ConvertDataFrames, BaseDBObject, StringMD5
from pandas.io.stata import StataReader

from com.transfer.utils.err import ErrorCode


class Stata(BaseDBObject):
    def __init__(self):
        super(Stata, self).__init__()
        self._uuid = StringMD5.md5(str(uuid.uuid4()))

    @staticmethod
    def __stata_2_dataframes(filename):
        _stata_data = StataReader(filename, convert_categoricals=False)
        return ConvertDataFrames.dataframes_split(_stata_data)

    def dataframes_2_db(self, filename, **kwargs):
        _time = kwargs.get("time", "")
        _table_data = kwargs.get("data_index", "data_index_default")
        _created = kwargs.get("created", "")
        _created_at = kwargs.get("created_at", time.time())
        _if_exists = kwargs.get("if_exists", "replace")
        _chunksize = kwargs.get("chunksize", 3000)
        _data, _data_dtypes, _variable_labels, _value_label = self.__stata_2_dataframes(filename)

        # _index_table
        _columns = _variable_labels.keys()
        # _types = _data_dtypes 废弃
        _varlabels = _variable_labels.values()
        _nrow = len(_columns)

        # _option_table
        _first_index, _second_index, _option_content = self.__value_labels(_value_label)

        _index_table = pd.DataFrame(
            {
                "uuid": self._uuid,
                "cid": _columns,
                # "type": _types,
                "title": _varlabels,
                "time": [_time] * _nrow,
                "created": [_created] * _nrow,
                "created_at": [_created_at] * _nrow
            }
        )

        _option_table = pd.DataFrame(
            {
                "cid": _first_index,
                "num_var": _second_index,
                "var": _option_content,
            }
        )
        try:
            print('----------------------------------------')
            _data.to_sql(
                self._uuid, con=self._stata_engine_data_base,flavor="mysql", if_exists=_if_exists,
                chunksize=_chunksize
            )
            print("========================================")
            _option_table.to_sql(
                self._uuid, con=self._stata_engine_data_options, if_exists=_if_exists,
                chunksize=_chunksize
            )
            _index_table.to_sql(
                _table_data, con=self._stata_engine_data_index, if_exists="append",
                chunksize=_chunksize, index=False, index_label="id"
            )
        except Exception as e:
            # self.__rollback_transaction(_table_data)
            print(e)
            raise ErrorCode.ERROR("SQL Data table write Error")
        finally:
            self.session.close()
        return ErrorCode.SUCCESS

    def read_db_2_dataframes(self):
        data = pd.read_sql_table(
            "e5fd2b6d-090f-4a07-b3d4-9aed200a6d12", self._stata_engine_data_index,
            schema='data_base',
            index_col='index'
        )
        data_dtype = data.dtypes

        print data_dtype

    def __value_labels(self, _value_label):
        _first_index, _second_index, _option_content = [], [], []
        [_first_index.extend([kvl] * len(vvl.keys())) for kvl, vvl in _value_label.items()]
        [_second_index.extend(vvl.keys()) for kvl, vvl in _value_label.items()]
        [_option_content.extend(vvl.values()) for kvl, vvl in _value_label.items()]
        return _first_index, _second_index, _option_content

    def __rollback_transaction(self, _table_data):
        try:
            self.session.execute('use :db', {'db': "data_base"})
            self.session.execute('drop table %s' % self._uuid)
        except Exception as e:
            self.logger.error(e)
            pass
        try:
            self.session.execute('use :db', {'db': "data_options"})
            self.session.execute('drop table %s' % self._uuid)
        except Exception as e:
            self.logger.error(e)
            pass
        try:
            self.session.execute('use :db', {'db': "data_index"})
            self.session.execute('delete from %s where UUID = %s' % (_table_data, self._uuid))
        except Exception as e:
            self.logger.error(e)
            pass
