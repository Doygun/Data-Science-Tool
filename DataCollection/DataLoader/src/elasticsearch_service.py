# coding=utf-8
"""

Elasticsearch Service
"""

__author__ = 'Seray Beser'

from elasticsearch import Elasticsearch
from DataCollection.DataLoader.src.abstract_service import AbstractService


class ElasticsearchService(AbstractService):
    """
    Elasticsearch Service for importing and exporting data

    """

    def __init__(self, url=None, __index__=None, __doc_type__=None):
        super(ElasticsearchService, self).__init__(url)
        self.client = Elasticsearch(hosts=url)
        self.index = __index__
        self.doc_type = __doc_type__

    def __str__(self):
        return 'Elasticsearch'

    def save_to_db(self, data):
        """
        Saves the data in the elasticsearch database
        :param data:
        """
        self.client.bulk(index=self.index, doc_type=self.doc_type, body=data,
                         request_timeout=500)

    def read_from_db(self, query):
        """
        Reads entries in the elasticsearch database by the query
        :param query:
        :return:
        """
        return self.client.search(index=self.index, body=query)

    def print_all_entry(self):
        """
        Prints all entries in the elasticsearch database
        """
        pass
