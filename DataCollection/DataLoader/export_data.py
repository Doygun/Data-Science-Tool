# coding=utf-8
"""

Exporting Data
"""

__author__ = 'Seray Beser'

from DataCollection.DataLoader.src.mongo_service import MongoService
from DataCollection.DataLoader.src.elasticsearch_service import ElasticsearchService


class ExportService(object):
    """
    Basic Usage:

    >> export_service = ExportService(service_name='Mongo', database_name='database_name',
                                   collection_name='collection_name')

    >> export_service.export_data(data=[{'name': 'seray'}])

    """

    def __init__(self, service_name=None, url=None, database_name=None, collection_name=None, index=None,
                 doc_type=None):
        """

        :param service_name: Mongo or Elasticsearch
        :param url: For Mongo url=localhost
        :param database_name: for Mongo Service
        :param collection_name: for Mongo Service
        :param index: for Elasticsearch
        :param doc_type: for ElasticSearch
        """
        self.name = str(service_name).lower()
        if self.name == 'mongo':
            self.service = MongoService(__database_name__=database_name, __collection_name__=collection_name)

        if self.name == 'elasticsearch':
            self.service = ElasticsearchService(url=url, __index__=index, __doc_type__=doc_type)

    def export_data(self, data):
        """
        exporting data
        :param data:
        """
        self.service.save_to_db(data)
