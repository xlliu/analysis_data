#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: spss.py
@time: 2016/7/27 14:40
"""
from pandas import pd
from pandas.io.stata import StataReader


class Spss(object):

    """
        Spss file type persistence into db
    """
    def __init__(self, filename):
        super(Spss, self).__init__()
        self._filename = filename

    def __spss_2_data(self):
        return "data", "name", "nameLabel", "type", "valueLable"

    @staticmethod
    def __into_db():
        data, name, nameLable, type, valueLable = Spss.__spss_2_data()

