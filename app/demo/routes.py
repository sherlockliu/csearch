from app.demo.hot_handler import HotHandler
from app.demo.hotel_handler import HotelHandler
from app.demo.hotel_list_handler import HotelListHandler
from app.demo.search_handler import SearchHandler

url_pattern = (
    (r'/hotel/([^/]+)/search/([^/]+)', SearchHandler), # step 4
    (r'/hotel/([^/]+)/hot/([^/]+)', HotHandler),       # step 3
    (r'/hotel/([^/]+)', HotelHandler),   # step 2
    (r'/hotel_list', HotelListHandler)   # step 1
)
