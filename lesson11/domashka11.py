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


def read_json_datafile(path):
    return json.load(open(path, "r"))


def sort_keys_by_text_len(names_dict):
    txt_list = names_dict['text'].split(' ')
    return len(txt_list)


def sort_keys_by_dod(names_dict):
    search = re.findall("\d+", names_dict['years'])
    # Здесь почему-то возника проблемка с кодировкой минус почемуто перекодировался
    txt_list = names_dict['years'].replace("\u2013", "-").split('-')
    bc_check = re.findall('bc', txt_list[-1], re.I)
    if not search:
        return 0
    year_of_death = int(search[-1])
    if bc_check:
        return year_of_death * -1
    return year_of_death




# zadanie 1
file_name = "datal.json"
json_data = ''

try:
    abspath = os.path.abspath(file_name)
    json_data = read_json_datafile(abspath)

except IOError as ex:
    print("%s: %s" % (file_name, ex.strerror))


# zadanie 2
if not json_data == '':
    sotrt_by_names = sorted(json_data, key=lambda n: n['name'].split(' ')[-1])
    pretty_print(sotrt_by_names)

    # zadanie 3
    sorted_by_dod = sorted(json_data, key=sort_keys_by_dod)

    # zadanie 4
    sorted_by_text_len = sorted(json_data, key=sort_keys_by_text_len)
else:
    print("Missing json_data or json file is empty")
