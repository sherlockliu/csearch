from elasticsearch import Elasticsearch


class ElasticSearchClient:
    def __init__(self):
        self.client = Elasticsearch()

    def create(self, index_name, doc_type, body):
        self.client.index(index=index_name, doc_type=doc_type, body=body)

    def search(self, index_name, doc_type, word_list: list):
        query_string = " AND ".join(word_list)
        res = self._search(index_name=index_name, doc_type=doc_type, body={
            "query": {
                "bool": {
                    "must": {
                        "query_string": {
                            "query": query_string,
                            "analyze_wildcard": True
                        }
                    }
                }
            }
        }, )
        return res

    def _search(self, index_name, doc_type, body):
        res = self.client.search(index=index_name, doc_type=doc_type, body=body, size=10000)
        return res

    def search_all(self):
        res = self._search("_all", "", {"query": {"match_all": {}}})
        return res

    def delete_all(self):
        self.client.delete_by_query("_all", {"query": {"match_all": {}}})
