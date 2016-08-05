import tornado.web
import tornado.ioloop


Handlers = [
    (r"/", MainHandler),
]
application = tornado.web.Application(Handlers)
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
