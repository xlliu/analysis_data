#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: db_engine.py
@time: 2016/7/29 17:36
"""
import os
import sys

from com.analysis.utils.conn import Conn

from com.analysis.utils.config import Config


class DBEngine(object):

    """
        database connetion engine
    """
    _cf = None

    def __init__(self):
        super(DBEngine, self).__init__()

    @staticmethod
    def __cur_file_dir():
        # 获取脚本路径
        return os.path.dirname(os.path.abspath(__file__))
        # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        # if os.path.isdir(path):
        #     return path
        # elif os.path.isfile(path):
        #     return os.path.dirname(path)

    @staticmethod
    def database_factory(**kwargs):
        global _cf
        _conf_url = "/".join([DBEngine.__cur_file_dir(), "conf.config"])
        print(_conf_url)
        _cf = Config(_conf_url)
        _stata_engine_default = None
        _stata_engine_data_options = None
        _stata_engine_data_base = None
        _stata_engine_data_index = None
        _db_data_index = _cf.get_content("db_data_index")
        _db_data_base = _cf.get_content("db_data_base")
        _db_default = _cf.get_content("db_default")
        _db_data_options = _cf.get_content("db_data_options")
        if kwargs.get("stata"):
            _stata_engine_default = Conn(
                hostname=_db_default.get("hostname"),
                port=_db_default.get("port"),
                db_name=_db_default.get("db_name"),
                user=_db_default.get("user"),
                pwd=_db_default.get("pwd")
            ).db_connect_engine()

        if kwargs.get("stata"):
            _stata_engine_data_options = Conn(
                hostname=_db_data_options.get("hostname"),
                port=_db_data_options.get("port"),
                db_name=_db_data_options.get("db_name"),
                user=_db_data_options.get("user"),
                pwd=_db_data_options.get("pwd")
            ).db_connect_engine()

        if kwargs.get("stata"):
            _stata_engine_data_base = Conn(
                hostname=_db_data_base.get("hostname"),
                port=_db_data_base.get("port"),
                db_name=_db_data_base.get("db_name"),
                user=_db_data_base.get("user"),
                pwd=_db_data_base.get("pwd")
            ).db_connect_engine()

        if kwargs.get("stata"):
            _stata_engine_data_index = Conn(
                hostname=_db_data_index.get("hostname"),
                port=_db_data_index.get("port"),
                db_name=_db_data_index.get("db_name"),
                user=_db_data_index.get("user"),
                pwd=_db_data_index.get("pwd")
            ).db_connect_engine()

        return _stata_engine_default, _stata_engine_data_index, _stata_engine_data_base, _stata_engine_data_options

