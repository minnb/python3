import csv
from collections import defaultdict


def read_csv(file_name: str) -> list:
    lst_data = list()
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row:
                lst_data.append(row[0].split(","))
    return lst_data


def region_list(data: list) -> set:
    region_data = set()
    for d in data[1:]:
        if d[0]:
            region_data.add(d[0])
    return sorted(region_data)


def type_list(data: list):
    for d in data[0:]:
        print(d[0], d[2])



# print(read_csv('data.csv'))
# print(region_list(read_csv('data.csv')))
type_list(read_csv('data.csv'))