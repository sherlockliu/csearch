from app.demo.hotel_handler import HotelHandler
from app.demo.search_handler import SearchHandler

url_pattern = (
    (r'/search/([^/]+)', SearchHandler),
    (r"/hotel/([^/]+)", HotelHandler)
)
