#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: db_operation.py
@time: 2016/8/3 16:42
"""
from com.transfer.convert.common import BaseDBObject


class OperationDataBase(BaseDBObject):
    def __init__(self):
        super(OperationDataBase, self).__init__()

    def drop_table(self):
        for db_name in self.session.execute('show databases').fetchall():
            if db_name[0] in self._db_list:
                print self.session.execute('drop database %s' %db_name[0])

    def create_table(self):
        for db_name in self._db_list:
            print self.session.execute('CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARSET utf8' %db_name)


if __name__ == '__main__':
    _od = OperationDataBase()
    _od.drop_table()
    _od.create_table()
    print "app run finish"