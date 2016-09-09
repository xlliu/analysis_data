#!/usr/bin/env python
# -*-  coding:utf-8 -*-
from tornado.web import Application

from tornado.ioloop import IOLoop

import tcelery
from com.analysis.handlers.data_analysis_handlers import *
from com.analysis.handlers.data_summany_handlers import *
# from com.analysis.handlers.defaulthandler import MainHandler, SleepHandler, JustNowHandler, GenAsyncHandler, Users
from com.analysis.handlers.defaulthandler import MainHandler

Handlers = [
    (r"/", MainHandler),
    # (r"/sleep", SleepHandler),
    # (r"/justnow", JustNowHandler),
    # (r"/genasyn", GenAsyncHandler),
    # (r"/user", Users),

    # todo  pass
    (r"/single_factor_variance_analysis/(.*)", SingleFactorVarianceAnalysis),
    # todo
    (r"/chisquaretest/(.*)", ChiSquareTest),
    # todo  pass
    (r"/frequency/(.*)", Frequency),
    # todo  pass
    (r"/meanvalue/(.*)", MeanValue),
    # todo  pass
    (r"/crosstable/(.*)", CrossTable),
    # todo
    (r"/datapivottable", DataPivotTable),
    # todo  pass
    (r"/correlationanalysis/(.*)", CorrelationAnalysis),
    # todo  pass
    (r"/generallinearregressionanalysis/(.*)", GeneralLinearRegressionAnalysis),
    (r"/valuesummany/(.*)", ValueSummany),
    
]

if __name__ == "__main__":
    tcelery.setup_nonblocking_producer()
    application = Application(Handlers)
    application.listen(port=8888, address="0.0.0.0")
    IOLoop.instance().start()
