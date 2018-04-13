# coding=utf-8
"""

Formatting Service
"""

import csv
import json
from pprint import pprint
import xmltodict
import xlrd

__author__ = 'Seray Beser'


class FormattingService(object):
    """
    Formatting Service

    Import is supported from following formats: csv,tsv,json,xml,xls
    Export is supported in following formats: csv,tsv,json,xml,xls


    """

    def __init__(self, form=None, path=None, header=False, save=False):
        self.form = form
        self.path = path
        self.header = header
        self.save = save
        self.data = list()
        self.data_header = list()

        self.open_file()

    def open_file(self):
        """
        open file
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
                return self.data, self.data_header

            if str(self.form).lower() == 'tsv':
                with open(self.path) as tsv_file:
                    rows = tsv_file.readlines()
                    for row in rows:
                        self.data.append(str(row).strip().split('\t'))
                if self.header:
                    self.data_header = self.data[0]
                    self.data.remove(self.data[0])
                return self.data, self.data_header

            if str(self.form).lower() == 'json':
                pass
            if str(self.form).lower() == 'xml':
                pass
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
                with open(self.path) as json_file:
                    data = json.loads(json_file.read())
                pprint(data)

            if str(self.form).lower() == 'xml':
                with open(self.path) as data_file:
                    data = data_file.read()
                pprint(json.loads(json.dumps(xmltodict.parse(data))))

            if str(self.form).lower() == 'xls':
                pprint(self.data_header)
                pprint(self.data)

        except IOError as e:
            print (e)

    def convert_csv(self):
        """
        convert_csv
        """
        pass

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
        pass


if __name__ == '__main__':
    fs = FormattingService(form='csv', path='deneme.csv')
    fs.print_file()
    print('-' * 100)

    fs = FormattingService(form='csv', path='deneme.csv', header=True)
    fs.print_file()
    print('-' * 100)

    fs = FormattingService(form='tsv', path='deneme_tsv.tsv')
    fs.print_file()
    print('-' * 100)

    fs = FormattingService(form='tsv', path='deneme_tsv.tsv', header=True)
    fs.print_file()
    print('-' * 100)

    fs = FormattingService(form='xls', path='tests-example.xls')
    fs.print_file()
    print('-' * 100)

    fs = FormattingService(form='xls', path='tests-example.xls', header=True)
    fs.print_file()
    print('-' * 100)

    # fs = FormattingService(form='json', path='deneme_json.json')
    # fs.print_file()
    # fs = FormattingService(form='xml', path='deneme_xml.xml')
