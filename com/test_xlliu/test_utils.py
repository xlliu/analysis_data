#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: test_utils.py
@time: 2016/8/9 11:12
"""

FILE_PATH = ""
f = open(FILE_PATH,"r")
longest = max(len(line) for line in f)
f.close()