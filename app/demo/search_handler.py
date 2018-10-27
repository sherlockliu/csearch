import json

from app.framework.handler.csearch_handler import CSearchHandler
from app.framework.textPreprocessing.text_processing_utils import get_similar_words, get_similar_sentence


class SearchHandler(CSearchHandler):
    def get(self, id, search_context):
        response = self._get_related_data(id, search_context)
        self.write(json.dumps(response))


    @staticmethod
    def _get_related_data(id, search_context):
        # wordss = get_similar_words(search_context)
        # question_list = get_similar_sentence(search_context)
        # comment_list = []
        # data_list = []
        # if wordss:
        #     for word in wordss[0]:
        #         comment = search_data("comment", word)
        #         if comment:
        #             comment_list.append(comment)
        #         data = search_data('data', word)
        #         if data:
        #             data_list.append(data)
        #     if not enough:
        #         for words in wordss[1]:
        #             for word in words:
        #                 comment = search_data("comment", word)
        #                 if comment:
        #                     comment_list.append(comment)
        #                 data = search_data('data', word)
        #                 if data:
        #                     data_list.append(data)
        # return {"comments": comment_list, "questions": question_list, "data": data_list}
        return {"comments": [{"id": "1", "title": "早餐", "context": "早餐很好吃", "author": "horison", "time": "2018-09-12 19:00:23"}], "questions": [], "data": []}