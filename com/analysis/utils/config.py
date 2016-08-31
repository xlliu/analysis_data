#!/usr/bin/env python
# -*-  coding:utf-8 -*-

"""
@version: 1.0.0
@author: xlliu
@contact: liu.xuelong@163.com
@site: https://github.com/xlliu
@software: PyCharm
@file: config.py
@time: 2016/8/2 13:45
"""
import ConfigParser


class Config(object):

    def __init__(self, config_filename):
        super(Config, self).__init__()
        print(config_filename)
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(config_filename)
        print(self.get_sections())

    def get_sections(self):
        return self.cf.sections()

    def get_options(self, section):
        return self.cf.options(section)

    def get_content(self, section):
        result = {}
        for option in self.get_options(section):
            value = self.cf.get(section, option)
            result[option] = int(value) if value.isdigit() else value
        return result


if __name__ == '__main__':
    _file_url = r"C:\Users\Administrator\PycharmProjects\transfer\com\conf.config"
    _cf = Config(_file_url)
    print _cf.get_content("db").get("xlliu2")