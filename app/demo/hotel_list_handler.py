import json

from app.framework.elastic_search_client import es_client
from app.framework.handler.csearch_handler import CSearchHandler
from app.framework.textPreprocessing.config import get_hotel_list


class HotelListHandler(CSearchHandler):
    def get(self):
        response = self._get_hotel_list()
        self.write(json.dumps(response))


    @staticmethod
    def _get_hotel_list():
        return [{"hotel_id": hotel[1], "hotel_name": hotel[0]} for hotel in get_hotel_list()[0:5]]