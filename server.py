# -*- coding: utf-8 -*-

import os

from app.preload import Preload
from ctrip.app_config import APPLICATION_SETTINGS
from ctrip.app_config import ROOT_LOCATION
from ctrip.routes import routes
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.web import Application


def start_server():
    define('port', default=8000, help='run on the given port', type=int)
    define("debug", default=False, help="whether is debug mode", type=bool)

    parse_command_line()

    APPLICATION_SETTINGS.update({
        "debug": options.debug,
        "template_path": os.path.join(
            ROOT_LOCATION,
            "app" if options.debug else "templates"
        ),
        "autoreload": True
    })
    application = Application(
        handlers=routes,
        **APPLICATION_SETTINGS
    )

    http_server = HTTPServer(application, xheaders=True)
    http_server.listen(options.port)
    print('Csearch is listening on 8000.')
    IOLoop.instance().start()


if __name__ == '__main__':
    Preload.preload_file_list()
    start_server()
