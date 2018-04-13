# coding=utf-8
"""

Importing Data
"""

__author__ = 'Seray Beser'

from DataCollection.DataLoader.src.mongo_service import MongoService
from DataCollection.DataLoader.src.elasticsearch_service import ElasticsearchService


class ImportService(object):
    """
    Basic Usage:

    >> import_service = ImportService(service_name='Mongo', database_name='database_name',
                                   collection_name='collection_name')

    >> print import_service.import_data(query={'name': 'seray'})

    >> import_service = ImportService(service_name='Elasticsearch', url='10.10.10.10:10', index='index_name')

    >> query = {
        "query": {"match_all": {}},
        "size": 1,
        "from": 2 }

    dump = import_service.import_data(query)

    for i in range(0, 1):
        print dump['hits']['hits'][i]['_source']['body']
    """

    def __init__(self, service_name=None, url=None, database_name=None, collection_name=None, index=None,
                 doc_type=None):
        """

        :param service_name: Mongo or Elasticsearch
        :param url: For Mongo url=localhost
        :param database_name: for Mongo Service
        :param collection_name: for Mongo Service
        :param index: for Elasticsearch Service
        :param doc_type: for Elasticsearch Service
        """
        self.name = str(service_name).lower()
        if self.name == 'mongo':
            self.service = MongoService(__database_name__=database_name, __collection_name__=collection_name)
        if self.name == 'elasticsearch':
            self.service = ElasticsearchService(url=url, __index__=index, __doc_type__=doc_type)

    def import_data(self, query):
        """
        importing data
        :param query:
        :return:
        """
        return self.service.read_from_db(query)

    def print_data(self):
        """
        printing data
        :return:
        """
        return self.service.print_all_entry()
