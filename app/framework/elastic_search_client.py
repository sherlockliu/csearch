from elasticsearch import Elasticsearch


class ElasticSearchClient:
    def __init__(self):
        self.client = Elasticsearch()

    def create(self, index_name, doc_type, body):
        self.client.index(index=index_name, doc_type=doc_type, body=body)

    def search_words_in_comments(self, id, word_list: list):
        query_string = '\"' + '\" AND \"'.join(word_list) + '\"'
        res = self._search(index_name="hotel_2*", doc_type="hotel_info", body={
            "query": {
                "bool": {
                    "must": [
                        {
                            "query_string": {
                                "query": query_string
                            }
                        },
                        {
                            "match": {
                                "hotel_id": {
                                    "query": id
                                }
                            }
                        }]
                }
            }
        })
        return res

    def search_words_in_data(self, id, word):
        res = self._search(index_name="hotel_11*", doc_type="hotel_info", body={
            "query": {
                "bool": {
                    "must": [
                        {
                            "query_string": {
                                "query": '"' + word + '"'
                            }
                        },
                        {
                            "match": {
                                "hotel_id": {
                                    "query": id
                                }
                            }
                        }]
                }
            }
        })
        return res

    def search_question_by_id(self, id, question_id):
        res = self._search(index_name="hotel_3*", doc_type="hotel_info", body={
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "question_id": {
                                    "query": question_id
                                }
                            }
                        },
                        {
                            "match": {
                                "hotel_id": {
                                    "query": id
                                }
                            }
                        }]
                }
            }
        })
        return res

    def search_hotel_list(self):
        res = self._search("hotel_0*", "", {"query": {"match_all": {}}})
        return res

    def _search(self, index_name, doc_type, body):
        res = self.client.search(index=index_name, doc_type=doc_type, body=body, size=10)
        return res

    def search_all(self):
        res = self._search("hotel_2*", "", {"query": {"match_all": {}}})
        return res

    def delete_all(self):
        self.client.delete_by_query("_all", {"query": {"match_all": {}}})

es_client = ElasticSearchClient()