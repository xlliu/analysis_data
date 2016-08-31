#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: conn.py
@time: 2016/7/29 10:59
"""

from sqlalchemy import create_engine


class Conn(object):

    """
    mysql connection
    """

    def __init__(self, hostname, port, db_name, user, **kwargs):
        super(Conn, self).__init__()
        self._hostname = hostname
        self._port = port
        self._db_name = db_name
        self._user = user
        self._pwd = kwargs.get("pwd", "")
        self._echo = kwargs.get("echo", False)

    def db_connect_engine(self):
        _conn_url = "mysql+pymysql://{user:s}:{pwd:s}@{hostname:s}:{port:d}/{db_name}?charset={charset}".format(
            user=self._user,
            pwd=self._pwd,
            hostname=self._hostname,
            port=self._port,
            db_name=self._db_name,
            charset="utf8"
        )
        engine = create_engine(_conn_url, echo=self._echo)
        return engine
