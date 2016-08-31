#!/usr/bin/env python
# -*-  coding:utf-8 -*-
from tornado.web import Application

from tornado.ioloop import IOLoop

import tcelery
from com.analysis.handlers.data_analysis_handlers import *
# from com.analysis.handlers.defaulthandler import MainHandler, SleepHandler, JustNowHandler, GenAsyncHandler, Users
from com.analysis.handlers.defaulthandler import MainHandler

Handlers = [
    (r"/", MainHandler),
    # (r"/sleep", SleepHandler),
    # (r"/justnow", JustNowHandler),
    # (r"/genasyn", GenAsyncHandler),
    # (r"/user", Users),

    # todo  pass
    (r"/single_factor_variance_analysis/(.*)_(.*)", SingleFactorVarianceAnalysis),
    # todo
    (r"/chisquaretest/(.*)_(.*)", ChiSquareTest),
    # todo  pass
    (r"/frequency/(.*)_(.*)", Frequency),
    # todo  pass
    (r"/meanvalue/(.*)_(.*)", MeanValue),
    # todo  pass
    (r"/crosstable/(.*)_(.*)", CrossTable),
    # todo
    (r"/datapivottable", DataPivotTable),
    # todo  pass
    (r"/correlationanalysis/(.*)_(.*)", CorrelationAnalysis),
    # todo  pass
    (r"/generallinearregressionanalysis/(.*)_(.*)", GeneralLinearRegressionAnalysis),
]

if __name__ == "__main__":
    tcelery.setup_nonblocking_producer()
    application = Application(Handlers)
    application.listen(port=8888, address="0.0.0.0")
    IOLoop.instance().start()
