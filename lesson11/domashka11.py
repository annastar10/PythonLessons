import json
import os
import re

'''
data.json - файл с данными о некоторых математиках прошлого.
1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
Если фамилии нет, то использовать имя, например Euclid.
3. Написать функцию сортировки по дате смерти из поля "years".
Обратите внимание на сокращение BC. - это означает до н.э.
4. Написать функцию сортировки по количеству слов в поле "text"
'''


def sort_keys_by_surname(names_dict):
    surname = names_dict['name'].split(' ').pop()
    return len(surname)


def read_json_datafile(path):
    return json.load(open(path, "r"))


def sort_keys_by_text_len(names_dict):
    txt_list = names_dict['text'].split(' ')
    return len(txt_list)


def sort_keys_by_dod(names_dict):
    search = re.findall("\d+", names_dict['years'])
    if search is None:
        return 0
    dod = int(search[1])
    dob = int(search[0])
    if dod - dob < 0:
        return dod * -1
    return dod


# zadanie 1
file_name = "data.json"
json_data = ''
if os.path.isfile(file_name):
    abspath = os.path.abspath(file_name)
    json_data = read_json_datafile(abspath)

# zadanie 2
if not json_data == '':
    sorted_by_names = sorted(json_data, key=sort_keys_by_surname)

    # zadanie 3
    sorted_by_dod = sorted(json_data, key=sort_keys_by_dod)

    # zadanie 4
    sorted_by_text_len = sorted(json_data, key=sort_keys_by_text_len)
