import csv


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


def type_list(data: list) -> set:
    type_data = set()
    for d in data[1:]:
        if d[2]:
            type_data.add((d[2]))
    return sorted(type_data)


def total_revenue(_data: list, _type: str):
    total = 0
    for d in _data[1:]:
        if d[2] == _type:
            total += float(d[11])
    return total


def total_revenue_by_type(_data: list):
    lst_type = type_list(_data)
    data = dict()
    for t in lst_type:
        data[t] = total_revenue(_data, t)
    return data


def main():
    again = True
    data_sales = read_csv('data.csv')
    while again:
        print("=======")
        print("1) List region")
        print("2) List type")
        print("3) Total revenue by type")
        print("4) List total revenue with type")
        print("5) Quit")
        print()
        selection = int(input("Enter your selection: "))
        if selection == 1:
            print(region_list(data_sales))
        elif selection == 2:
            print(type_list(data_sales))
        elif selection == 3:
            print(total_revenue(data_sales, "Baby Food"))
        elif selection == 4:
            print(total_revenue_by_type(data_sales))
        elif selection == 5:
            print("Good bye!!!")
            again = False
        else:
            print("Incorrect selection")


main()
