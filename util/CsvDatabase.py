#!usr/bin/env python
#coding:utf-8

import csv


class CsvDatabase:
    def __init__(self, filename):
        self.filename = filename

    def saveData(self, data):
        #with open(self.filename, 'a') as csvfile:
        for item in data:
            self.writer.writerow(item)

    def buildColumn(self, columns):
        self.csvfile = open(self.filename, 'w')
        self.writer = csv.DictWriter(self.csvfile, fieldnames=columns)
        self.writer.writeheader()

    def close(self):
        self.csvfile.close()

if __name__ == '__main__':
    fieldnames = ['first_name', 'last_name']
    filename = 'names.csv'
    csvDb = CsvDatabase(filename)
    csvDb.buildColumn(fieldnames)
    data = [{'first_name': 'Baked', 'last_name': 'Beans'}, {'first_name': 'Baked', 'last_name': 'Beans'}, {'first_name': 'Baked', 'last_name': 'Beans'}]
    csvDb.saveData(data)