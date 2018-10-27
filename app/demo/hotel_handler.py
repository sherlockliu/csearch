import json

from app.framework.handler.csearch_handler import CSearchHandler


class HotelHandler(CSearchHandler):
    def get(self, id):
        response = self._get_hotel_by_id(id)
        self.write(json.dumps(response))

    @staticmethod
    def _get_hotel_by_id(id):
        # return get_hot(id)
        return ["早餐", "加床"]