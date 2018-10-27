from tornado.web import RequestHandler


class CSearchHandler(RequestHandler):
    def initialize(self):
        print('Handler Init!')
