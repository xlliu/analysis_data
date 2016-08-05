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
import os

from com.transfer.core.stata import Stata


def file_extry(dir, time):
    # dir = r"C:\Users\Administrator\PycharmProjects\transfer\test_data"
    for filename in os.listdir(dir):
        filename_all = dir + "\\" + filename
        s = Stata()
        s.dataframes_2_db(filename_all, time=time)
        # if "cgss" in filename:
        #     pass
            # datatime = filename[4:8]
            # s.read_db_2_dataframes()
    print "data into db finish"


if __name__ == '__main__':
    pass