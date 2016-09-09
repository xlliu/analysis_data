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
import sys
sys.path.append('../..')
from com.transfer.core.stata import Stata
from com.transfer.convert.theme import Theme
from com.transfer.convert.theme import MergeTable

def file_extry():
    # dir = r"C:\Users\Administrator\PycharmProjects\analysis\com\test_data"
    dir = r"/home/xuelong/8.30data"

    for filename in os.listdir(dir):
        filename_all = dir + "/" + filename
        if "dta" in filename:
            print(filename_all)
            s = Stata()
            time = filename[4:8]
            s.dataframes_2_db(filename_all, time=time)
            # s.read_db_2_dataframes()
    print "data into db finish"


def theme_extry():
    dir = r"/home/xuelong/data_theme3.xlsx"
    Theme(dir)

def merge_table():
    result = MergeTable().met()
    print result

if __name__ == '__main__':
    # file_extry()
    # theme_extry()
    merge_table()
    
