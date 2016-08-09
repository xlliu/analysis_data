#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: common.py
@time: 2016/7/29 17:20
"""
import hashlib
import time

from com.transfer.db.db_engine import DBEngine
from sqlalchemy.orm import sessionmaker

from com.transfer.utils.log import LogCF


class BaseObject(object):

    @LogCF.open_log(True)
    def __init__(self, **kwargs):
        self.logger = kwargs.get("logger")


class BaseDBObject(BaseObject):

    def __init__(self):
        super(BaseDBObject, self).__init__()
        self._stata_engine_default, \
        self._stata_engine_data_index, \
        self._stata_engine_data_base, \
        self._stata_engine_data_options = DBEngine.database_factory(stata=True)
        _DB_session = sessionmaker(bind=self._stata_engine_default)
        self.session = _DB_session()
        self._db_list = ["data_base", "data_index", "data_options"]


class ConvertDataFrames(object):

    """
        Common component

            data to dataframes
    """

    def __init__(self):
        super(ConvertDataFrames, self).__init__()

    @staticmethod
    def dataframes_split(dataframes):
        _data = dataframes.data()
        _data_dtypes = dataframes.dtyplist
        _data_variable_labels = dataframes.variable_labels()
        _data_value_labels = dataframes.value_labels()
        return _data, _data_dtypes, _data_variable_labels, _data_value_labels


class ConvertTime(object):

    """
        About time convert
    """

    @staticmethod
    def time_2_timestamp(time, **kwargs):

        time_frame = kwargs.get("timeframe", "%Y-%m-%d %H:%M:%S")
        # a = "2013-10-10 23:40:00"
        time_array = time.strptime(time, time_frame)
        # 转换为时间戳:
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    @staticmethod
    def timestamp_2_time(timestamp, **kwargs):
        time_frame = kwargs.get("timeframe", "%Y-%m-%d %H:%M:%S")
        # a = "2013-10-10 23:40:00"
        time_array = time.localtime(timestamp)
        time_str = time.strftime(time_frame, time_array)
        return time_str


class StringMD5(object):

    def __init__(self):
        pass

    @staticmethod
    def md5(str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
