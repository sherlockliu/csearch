import json

from app.framework.elastic_search_client import es_client
from app.framework.handler.csearch_handler import CSearchHandler
# from app.framework.textPreprocessing.text_processing_utils import get_similar_words


class HotHandler(CSearchHandler):
    def get(self, id, input_context):
        hot_list, suggestion_list = self._get_hot(id, input_context)
        # if not hot_list and not suggestion_list:
            # context = jiucuo()
            # hot_list, suggestion_list = self._get_hot(context)
        self.write(json.dumps({"hots": hot_list, "suggestions": suggestion_list}))

    def _get_hot(self, id, input_context):
        # wordss = get_similar_words(input_context)  # [["酒店", "早餐"],[["旅店"]["早饭"]]
        wordss = [['酒店', '早餐'], [('大酒店', 0.7869350910186768), ('饭店', 0.7779560089111328), ('国际酒店', 0.772890567779541),
                             ('西式早餐', 0.708486795425415), ('单早', 0.6782412528991699), ('双早', 0.6766752004623413)]]
        hot_list = []
        suggestion_list = []
        if wordss:
            for word in wordss[0]:
                hot_list.extend(self._search_hot(id, word))
            if len(hot_list) < 5:
                for words in wordss[1]:
                    hot_list.extend(self._search_hot(id, words[0]))
            word_list = wordss[0]
            suggestion_list.extend(self._search_suggest(id, word_list))
            while len(word_list) > 1:
                if len(suggestion_list) >= 5:
                    break
                else:
                    word_list.pop()
                    suggestion_list.extend(self._search_suggest(id, word_list))

            if len(suggestion_list) < 5:
                for words in wordss[1]:
                    suggestion_list.extend(self._search_suggest(id, [words[0]]))
        return hot_list, suggestion_list

        # if input_context == "早":
        #     return {"hot": ["早餐"], "suggestion": ["有没有早餐", "早餐多少钱", "早餐时间是到几点"]}
        # else:  # input 有
        #     return {"hot": [], "suggestion": ["有没有早餐", "有没有餐厅", "有没有加床"]}

    def _search_hot(self, id, word):
        return self._parse_result(es_client.search_hot(id, word))

    def _search_suggest(self, id, word_list):
        return self._parse_result(es_client.search_suggestion(id, word_list))

    @staticmethod
    def _parse_result(result):
        if result.get('hits', {}).get('hits', []):
            return [hits.get('_source') for hits in result.get('hits').get('hits')]