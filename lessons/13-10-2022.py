import csv
import sys

# delimeter - это запятая, которая разделяет
# quotechar - символ экранирования
future_csv_data = list()
with open('test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(spamreader):
        print(f'{i} row')
        future_csv_data.append(row)

print('#' * 50)

with open('test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(row)

print(row)

# pandas - расширенный модуль для работы с csv

print('#' * 50)

with open('test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    print('Size: ', sys.getsizeof(csvfile))  # размер объекта
    for row in future_csv_data:
        spamwriter.writerow(row)
    spamwriter.writerow(['this is', 'writen by', 'csv', 'writer'])

print('#' * 50)
xlist = [i for i in range(11)]
xxgen = (i for i in range(10))
print(xlist, '\n', xxgen)
print('Size: xlist', sys.getsizeof(xlist))
print('Size: xxgen', sys.getsizeof(xxgen))

print('#' * 50)


def my_generator_fun(list_to_convert: list):
    for x in list_to_convert:
        print('1 about to generate: ', x)
        yield x
        print('3 just to generate: ', x)


for element in my_generator_fun(([x for x in range(5)])):
    print(2, element)
