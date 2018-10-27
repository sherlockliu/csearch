import json

from app.framework.handler.csearch_handler import CSearchHandler


class HotelListHandler(CSearchHandler):
    def get(self):
        response = self._get_hotel_list()
        self.write(json.dumps(response))


    @staticmethod
    def _get_hotel_list():
        # return get_hotel_list()
        return [{"id": 346693, "name": "三亚亚龙湾华宇度假酒店"}]