import json

from app.framework.handler.csearch_handler import CSearchHandler
from app.framework.textPreprocessing.text_processing_utils import get_similar_words


class HotHandler(CSearchHandler):
    def get(self, id, input_context):
        hot_list, suggestion_list = self._get_hot(id, input_context)
        # if not hot_list and not suggestion_list:
            # context = jiucuo()
            # hot_list, suggestion_list = self._get_hot(context)
        # self.write(json.dumps({"hots": hot_list, "suggestions": suggestion_list}))

    @staticmethod
    def _get_hot(id, input_context):
        # wordss = get_similar_words(input_context)  # [["酒店", "早餐"],[["旅店"]["早饭"]]
        # hot_list = []
        # suggestion_list = []
        # if wordss:
        #     for word in wordss[0]:
        #         result = search_data("hot", word)
        #         suggestion = search_data("suggestion", word)
        #         if result:
        #             hot_list.append(result)
        #         if suggestion:
        #             suggestion_list.append(suggestion)
        #     if not enough:
        #         for words in wordss[1]:
        #             for word in words:
        #                 result = search_data("hot", word)
        #                 suggestion = search_data("suggestion", word)
        #                 if result:
        #                     hot_list.append(result)
        #                 if suggestion:
        #                     suggestion_list.append(suggestion)
        # return hot_list, suggestion_list

        if input_context == "早":
            return {"hot": ["早餐"], "suggestion": ["有没有早餐", "早餐多少钱", "早餐时间是到几点"]}
        else:  # input 有
            return {"hot": [], "suggestion": ["有没有早餐", "有没有餐厅", "有没有加床"]}