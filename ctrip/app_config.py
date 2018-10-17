# -*- coding: utf-8 -*-

import os

ROOT_LOCATION = os.path.dirname(os.path.dirname(__file__))

APPLICATION_SETTINGS = {
    # NOTE: please use nginx to serve static file in production enviroment
    'static_path': ROOT_LOCATION + '/static/'
}

