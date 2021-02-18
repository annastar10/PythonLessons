import csv
import json
import os
import random as rnd

'''
1. Написать функцию read_file которая принимает один параметр - полный путь к файлу.
В зависимости от расширения файла (txt, csv, json) считывает и возвращает данные из файла.
Для csv использовать reader и writer.
Если расширение не соответствует заданным, то вывести текст "Unsupported file format"

2. Написать функцию write_file которая принимает два параметра - полный путь к файлу и данные.
В зависимости от расширения файла (txt, csv, json) записывает данные в данный файл.
Для csv использовать DictReader и DictWriter.
Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
Данные для записи и файлы создать самим. Файлы с результатами добавить в гит.
'''


def read_file(path: str):
    fname, file_ext = os.path.splitext(path)
    if file_ext == '.csv':
        return list(csv.DictReader(open(path)))
    elif file_ext == '.txt':
        return open(path, "r").read()
    elif file_ext == '.json':
        return json.load(open(path, "r"))
    else:
        print('Unsupported file format')
        return 0


def write_file(path: str, data):
    fname, file_ext = os.path.splitext(path)
    if file_ext == '.csv':
        keys = data[0].keys()
        with open(path, 'w', newline='')  as out_file:
            dict_writer = csv.DictWriter(out_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    elif file_ext == '.txt':
        return open(path, "w").write(data)
    elif file_ext == '.json':
        with open(path, 'w') as fp:
            json.dump(data, fp, indent=4)


# zadanie 1
files = ["cities.csv", "text.txt", "address.json", "text.doc"]
file = rnd.choice(files)
content = 0
if os.path.isfile(file):
    path = os.path.abspath(file)
    content = read_file(path)


# zadanie 2
# Будем использовать в качестве данных для записи, полученный контент из задания 1
file_name2_path = os.path.abspath("out_" + file)
if not content == 0:
    write_file(file_name2_path, content)
else:
    print('Unsupported file format to write')
