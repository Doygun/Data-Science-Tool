# coding=utf-8
"""

Formatting Service
"""

import csv
import json
from pprint import pprint
import xmltodict
import xlrd

import pandas as pd

__author__ = 'Seray Beser'


class FormattingService(object):
    """
    Formatting Service

    Import is supported from following formats: csv,tsv,json,xml,xls
    Export is supported in following formats: csv,tsv,json,xml,xls


    """

    def __init__(self, form=None, path=None, header=False, save=False, header_names=None):
        self.form = form
        self.path = path
        self.header = header
        self.save = save
        self.data = list()
        self.data_header = list()
        self.header_names = header_names
        self.open_file()

        if self.header_names:
            self.data_header = self.header_names

    def open_file(self):
        """
        open file
        :return data, data_header
        """
        try:
            if str(self.form).lower() == 'csv':
                with open(self.path, 'rb') as csv_file:
                    rows = csv.reader(csv_file)
                    for row in rows:
                        self.data.append(row)
                if self.header:
                    self.data_header = self.data[0]
                    self.data.remove(self.data[0])
                self.fill_none()
                return self.data, self.data_header

            if str(self.form).lower() == 'tsv':
                with open(self.path) as tsv_file:
                    rows = tsv_file.readlines()
                    for row in rows:
                        self.data.append(str(row).strip().split('\t'))
                if self.header:
                    self.data_header = self.data[0]
                    self.data.remove(self.data[0])
                self.fill_none()
                return self.data, self.data_header

            if str(self.form).lower() == 'json':
                with open(self.path) as json_file:
                    self.data = json.loads(json_file.read())

            if str(self.form).lower() == 'xml':
                with open(self.path) as data_file:
                    data = data_file.read()
                self.data = json.loads(json.dumps(xmltodict.parse(data)))

            if str(self.form).lower() == 'xls':
                workbook = xlrd.open_workbook(self.path)
                worksheet = workbook.sheet_by_index(0)
                if self.header:
                    for column in range(worksheet.ncols):
                        self.data_header.append(worksheet.cell_value(0, column))
                    for row in range(1, worksheet.nrows):
                        value = list()
                        for column in range(worksheet.ncols):
                            value.append(worksheet.cell_value(row, column))
                        self.data.append(value)
                if not self.header:
                    for row in range(0, worksheet.nrows):
                        value = list()
                        for column in range(worksheet.ncols):
                            value.append(worksheet.cell_value(row, column))
                        self.data.append(value)
                self.fill_none()
                return self.data, self.data_header

        except IOError as e:
            print (e)

    def print_file(self):
        """
        open file
        """
        try:
            if str(self.form).lower() == 'csv':
                pprint(self.data_header)
                pprint(self.data)

            if str(self.form).lower() == 'tsv':
                pprint(self.data_header)
                pprint(self.data)

            if str(self.form).lower() == 'json':
                pprint(self.data)

            if str(self.form).lower() == 'xml':
                pprint(self.data)

            if str(self.form).lower() == 'xls':
                pprint(self.data_header)
                pprint(self.data)

        except IOError as e:
            print (e)

    def fill_none(self):
        """

        :return:
        """
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[0])):
                if len(str(self.data[i][j])) == 0:
                    self.data[i][j] = None

        for i in range(0, len(self.data_header)):
            if len(str(self.data_header[i])) == 0:
                self.data_header[i] = None

    def convert_csv(self):
        """
        convert_csv
        """
        with open(str(self.path) + '_new.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(self.data_header)
            for row in self.data:
                csv_writer.writerow(row)

    def convert_json(self):
        """
        convert_json
        """
        pass

    def convert_tsv(self):
        """
        convert_tsv
        """
        pass

    def convert_xml(self):
        """
        convert_xml
        """
        pass

    def convert_xls(self):
        """
        convert_xls
        """
        pass

    def convert_dataframe(self):
        """
        convert_dataframe
        """
        if self.header or self.header_names:
            return pd.DataFrame(self.data, columns=self.data_header)
        else:
            return pd.DataFrame(self.data)


def test():
    """
    test method for FormattingService
    """
    fs = FormattingService(form='csv', path='example.csv', header_names=["col 1", "col 2", "col 3", "col 4"])
    # fs.print_file()
    print(fs.convert_dataframe())
    print('-' * 100)

    fs = FormattingService(form='csv', path='example.csv', header=True)
    # fs.print_file()
    print(fs.convert_dataframe())
    print('-' * 100)

    fs = FormattingService(form='tsv', path='example.tsv')
    # fs.print_file()
    print(fs.convert_dataframe())
    print('-' * 100)

    fs = FormattingService(form='tsv', path='example.tsv', header=True)
    # fs.print_file()
    print(fs.convert_dataframe())
    print('-' * 100)
    # fs.convert_csv()

    fs = FormattingService(form='xls', path='example.xls')
    # fs.convert_csv()
    # fs.print_file()
    print(fs.convert_dataframe())
    print('-' * 100)

    fs = FormattingService(form='xls', path='example.xls', header=True)
    # fs.print_file()
    print(fs.convert_dataframe())
    print('-' * 100)

    fs = FormattingService(form='json', path='example.json')
    # fs.print_file()
    # fs.convert_csv()
    print(fs.convert_dataframe())
    print('-' * 100)

    fs = FormattingService(form='xml', path='example.xml')
    # fs.print_file()
    print(fs.convert_dataframe())

    print('-' * 100)


if __name__ == '__main__':
    test()
