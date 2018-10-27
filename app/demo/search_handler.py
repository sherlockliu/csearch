import json

from app.framework.handler.csearch_handler import CSearchHandler


class SearchHandler(CSearchHandler):
    def get(self, search_context):
        response = self._get_related_data(search_context)
        self.write(json.dumps(response))


    @staticmethod
    def _get_related_data(search_context):
        return {"context": search_context}