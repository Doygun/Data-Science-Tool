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

from DataPreprocessing.src.data_cleaning import DataCleaning
from DataPreprocessing.formatting_service import FormattingService


class PreprocessService(object):
    """
    Preprocess Service

    Basic Usage:

    >>      preprocess = PreprocessService(data=data)
    >>      service = preprocess.service('Cleaning')

    >>      # cleaning rows
    >>      data = service.clean_missing_value_row()

    """

    def __init__(self, data=None):
        self.data = data

    def service(self, preprocess_name=None):
        """

        :return:
        """
        if str(preprocess_name).lower() == 'cleaning':
            return DataCleaning(data=self.data)


def cleaning_service_test():
    """

    test method for preprocess service
    """

    fs = FormattingService(form='csv', path='test_data/example.csv', header=True)
    data = fs.convert_dataframe()
    print("Raw Data:")
    print(data)

    preprocess = PreprocessService(data=data)
    service = preprocess.service('Cleaning')

    # cleaning rows
    data = service.clean_missing_value_row()

    print("\nAfter Cleaning Missing Value Row:")
    print(data)

    # cleaning columns
    data = service.clean_missing_value_column()

    print("\nAfter Cleaning Missing Value Column:")
    print(data)

    # cleaning duplicate rows
    data = service.clean_duplicate_rows()

    print("\nAfter Cleaning Duplicate Rows:")
    print(data)

    # cleaning duplicate columns
    data = service.clean_duplicate_columns()

    print("\nAfter Cleaning Duplicate Columns:")
    print(data)

    # cleaning 1. row
    data = service.clean_row(1)

    print("\nAfter Cleaning 1. Row:")
    print(data)

    # cleaning 2. and 3. row
    data = service.clean_row([2, 3])

    print("\nAfter Cleaning 2. and 3. Row:")
    print(data)

    # cleaning 1. column
    data = service.clean_column('column_1')

    print("\nAfter Cleaning 1. Column:")
    print(data)

    # cleaning 2. and 3. column
    data = service.clean_column(['column_2', 'column_3'])

    print("\nAfter Cleaning 2. and 3. Column:")
    print(data)


if __name__ == '__main__':
    cleaning_service_test()
