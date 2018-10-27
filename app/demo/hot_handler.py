import json

from app.framework.handler.csearch_handler import CSearchHandler
from app.framework.textPreprocessing.text_processing_utils import get_similar_words, get_pinyin_words, get_least_levenshtein
from app.framework.textPreprocessing.config import HIGHFREQUENCYSEARCH, QUESTION


class HotHandler(CSearchHandler):
    def get(self, id, input_context):
        hot_list, suggestion_list = self._get_hot(id, input_context)
        self.write(json.dumps({"hots": hot_list, "suggestions": suggestion_list}))

    def _get_hot(self, id, input_context):
        wordss = get_similar_words(input_context, 3)  # [["酒店", "早餐"],[["旅店"]["早饭"]]
        # wordss = [['早餐'], [('大酒店', 0.7869350910186768), ('饭店', 0.7779560089111328), ('国际酒店', 0.772890567779541),
        #                      ('西式早餐', 0.708486795425415), ('单早', 0.6782412528991699), ('双早', 0.6766752004623413)]]
        hot_list = []
        suggestion_list = []
        if wordss:
            for word in wordss[0]:
                hot_list.extend(self._search_hot(word))
            if len(hot_list) < 5:
                for words in wordss[1]:
                    hot_list.extend(self._search_hot(words[0]))

            for word in wordss[0]:
                suggestion_list.extend(self._search_suggest(word))
            if len(suggestion_list) < 5:
                for words in wordss[1]:
                    suggestion_list.extend(self._search_suggest(words[0]))

        return list(set(hot_list)), list(set(suggestion_list))

        # if input_context == "早":
        #     return {"hot": ["早餐"], "suggestion": ["有没有早餐", "早餐多少钱", "早餐时间是到几点"]}
        # else:  # input 有
        #     return {"hot": [], "suggestion": ["有没有早餐", "有没有餐厅", "有没有加床"]}

    def _search_hot(self, word):
        hot_word_list = []
        for hot_word in HIGHFREQUENCYSEARCH:
            if word in hot_word:
                hot_word_list.append(hot_word)
        if not hot_word_list and len(word) < 4:
            new_word = get_pinyin_words(word)
            if new_word:
                for hot_word in HIGHFREQUENCYSEARCH:
                    if new_word in hot_word:
                        hot_word_list.append(hot_word)
        if not hot_word_list and len(word) < 4 and len(word) > 1:
            new_word = get_least_levenshtein(word)
            if new_word:
                for hot_word in HIGHFREQUENCYSEARCH:
                    if new_word in hot_word:
                        hot_word_list.append(hot_word)

        return hot_word_list

    def _search_suggest(self, word):
        suggest_question_list = []
        for suggest_question in QUESTION:
            if word in suggest_question:
                suggest_question_list.append(suggest_question)
        return suggest_question_list
