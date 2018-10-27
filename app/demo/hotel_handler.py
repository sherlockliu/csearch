import json

from app.framework.handler.csearch_handler import CSearchHandler
from app.framework.textPreprocessing.config import get_highFrequencySearch


class HotelHandler(CSearchHandler):
    def get(self, id):
        response = self._get_hotel_by_id(id)
        self.write(json.dumps(response))

    @staticmethod
    def _get_hotel_by_id(id):
        return get_highFrequencySearch()[0:5]