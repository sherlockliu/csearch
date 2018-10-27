import json

from app.framework.handler.csearch_handler import CSearchHandler
# from app.framework.textPreprocessing.text_processing_utils import get_similar_words, get_similar_sentence
from app.framework.elastic_search_client import es_client


class SearchHandler(CSearchHandler):
    def get(self, id, search_context):
        response = self._get_related_data(id, search_context)
        self.write(json.dumps(response))


    def _get_related_data(self, id, search_context):
        # wordss = get_similar_words(search_context)
        # question_list = get_similar_sentence(search_context)
        wordss = [['窗户'], [('西式早餐', 0.708486795425415), ('单早', 0.6782412528991699), ('双早', 0.6766752004623413)]]
        question_list = self._search_questions_by_ids([5502021, 5250280, 4459035])
        comment_list = []
        data_list = []
        if wordss:
            word_list = wordss[0]
            comment_list.extend(self._search_words_in_comments(id, word_list))
            while len(word_list) > 1:
                if len(comment_list) >= 5:
                    break
                else:
                    word_list.pop()
                    comment_list.extend(self._search_words_in_comments(id, word_list))
            word_list = wordss[0]
            data_list.extend(self._search_words_in_data(id, word_list))
            while len(word_list) > 1:
                if len(data_list) >= 5:
                    break
                else:
                    word_list.pop()
                    data_list.extend(self._search_words_in_data(id, word_list))

            if len(data_list) < 5:
                for words in wordss[1]:
                    data_list.extend(self._search_words_in_data(id, [words[0]]))
        return {"comments": comment_list, "questions": question_list, "data": data_list}
        # return {"comments": [{"id": "1", "title": "早餐", "context": "早餐很好吃", "author": "horison", "time": "2018-09-12 19:00:23"}], "questions": [], "data": []}

    def _search_words_in_comments(self, id, word_list):
        # result = es_client.search_words_in_comments(id, word_list)
        # return self._parse_comment_result(result)
        return []

    def _search_words_in_data(self, id, word_list):
        result = es_client.search_words_in_data(id, word_list)
        return self._parse_data_result(result)

    @staticmethod
    def _search_questions_by_ids(ids: list):
        question_list = []
        for id in ids:
            question = es_client.search_question_by_id(id)
            if question:
                question_list.append(question)
        return question_list

    @staticmethod
    def _parse_comment_result(result):
        if result.get('hits', {}).get('hits', []):
            return [hits.get('_source') for hits in result.get('hits').get('hits')]

    @staticmethod
    def _parse_data_result(result):
        if result.get('hits', {}).get('hits', []):
            return [hits.get('_source') for hits in result.get('hits').get('hits')]