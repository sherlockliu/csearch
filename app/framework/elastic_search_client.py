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


es = ElasticSearchClient()
es.create('test_index', 'test_type', {'data': 'test_data', 'ts': datetime.now()})
result = es.search('test_index*', 'test_type', body={"query": {"match_all":{}}})
print(result['hits']['hits'][0]['_source'])