from app.framework.handler.csearch_handler import CSearchHandler
import app.demo.routes

routes = ()

# all routes goes here...
routes += app.demo.routes.url_pattern
routes += (
    (r'.*', CSearchHandler),
)
