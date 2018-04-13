# coding=utf-8
"""

Abstract Service
"""

__author__ = 'Seray Beser'

from abc import abstractmethod


class AbstractService(object):
    """
    Abstract Service for importing and exporting data

    """

    def __init__(self, url='localhost'):
        """
        :param url: Default url is `localhost`
        """
        self.url = url

    @abstractmethod
    def save_to_db(self, data):
        """
        Saves the data in the database
        :param data:
        """
        pass

    @abstractmethod
    def read_from_db(self, query):
        """
        Reads entries in the database by the query
        :param query:
        """
        pass

    @abstractmethod
    def print_all_entry(self):
        """
        Prints all entries in the database
        """
        pass
