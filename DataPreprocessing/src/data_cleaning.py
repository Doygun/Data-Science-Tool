# coding=utf-8
"""

Data Cleaning
"""
__author__ = 'Seray Beser'
__copyright__ = 'Copyright 2018 Seray Beser'
__license__ = 'Apache License 2.0'
__version__ = '0.0.1'
__email__ = 'seraybeserr@gmail.com'
__status__ = 'Development'


class DataCleaning(object):
    """
    Data Cleaning
    """

    def __init__(self, data):
        self.data = data

    def clean_missing_value_row(self):
        """
        clean_missing_value_row
        :return:
        """
        return self.data.dropna()

    def clean_missing_value_column(self):
        """
        clean_missing_value_column
        :return:
        """
        return self.data.dropna(axis=1)

    def clean_duplicate_rows(self):
        """
        clean_duplicate_rows
        :return:
        """
        return self.data.drop_duplicates()

    def clean_duplicate_columns(self):
        """
        clean_duplicate_rows
        :return:

        """
        return self.data.T.drop_duplicates().T

    def clean_row(self, rows):
        """
        :param rows:
        :return:
        """
        return self.data.drop(rows)

    def clean_column(self, columns):
        """
        :param columns:
        :return:
        """
        return self.data.drop(columns, axis=1)
