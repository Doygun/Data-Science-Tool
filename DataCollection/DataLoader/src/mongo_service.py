# coding=utf-8
"""

MongoDb Service
"""

__author__ = 'Seray Beser'

from pymongo import MongoClient
from DataCollection.DataLoader.src.abstract_service import AbstractService


class MongoService(AbstractService):
    """
    Mongo Service for importing and exporting data

    """

    def __init__(self, url=None, port=27017, __database_name__=None, __collection_name__=None):
        super(MongoService, self).__init__(url)
        self.client = MongoClient(host=url, port=port)
        self.database = self.client[__database_name__]
        self.collection = self.database[__collection_name__]

    def __str__(self):
        return 'Mongo'

    def read_from_db(self, query):
        """
        Reads entries in the mongo database by the query
        :param query:
        :return:
        """
        return self.collection.find_one(query)

    def save_to_db(self, data):
        """
        Saves the data in the mongo database
        :param data:
        """
        self.collection.insert_many(data)

    def print_all_entry(self):
        """
        Prints all entries in the mongo database
        """
        dump = self.collection.find({})
        for document in dump:
            print (document)
