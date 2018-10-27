from datetime import datetime
from elasticsearch import Elasticsearch


class ElasticSearchClient:
    def __init__(self):
        self.client = Elasticsearch()

    def create(self, index_name, doc_type, body):
        self.client.index(index=index_name, doc_type=doc_type, body=body, ignore=400)

    def search(self, index_name, doc_type, body):
        res = self.client.search(index=index_name, doc_type=doc_type, body=body)
        return res
    