import csv
import json
import os
import re
from random import randint

import requests

quote_qty = 5
csv_filename = os.path.abspath('quotes.csv')
authors_path = os.path.abspath('authors.txt')
authors_json = os.path.abspath('authors.json')

url = "http://api.forismatic.com/api/1.0/"
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']


def get_rnd_quotes(qty: int):
    unique_quotes = []
    min_rnd_seed = 1
    max_rnd_seed = 10000
    # увеличиваем количество в 2 раза чтобы получить требуемое количество в случае повторов цитат
    for number in range(1, qty * 2):
        params = {"method": "getQuote",
                  "format": "json",
                  "key": randint(min_rnd_seed, max_rnd_seed),
                  "lang": "ru"}
        response = requests.get(url, params=params)
        if not response.status_code == 200:
            continue
        new_quote = response.json()
        author = new_quote.get("quoteAuthor")
        quote = new_quote.get("quoteText")
        quote_url = new_quote.get("quoteLink")
        single_quote = {"Author": author, "Quote": quote, "URL": quote_url}
        if (author == '' or quote == '' or quote_url == '') or (single_quote in unique_quotes):
            continue
        unique_quotes.append(single_quote)
        if len(unique_quotes) >= qty:
            break
    return unique_quotes


def read_txt_file(path: str):
    read_txt = open(path, "r").read()
    return re.findall("(?P<date>\\d+[^-]+)\\s+\\-\\s+(?P<author>.+)\\s+(birthday|death),\\s+author of (?P<story>.+)",
                      read_txt, flags=re.I)


def convert_date(date: str):
    searches = re.search("(?P<dd>\\d+)\\w+\\s+(?P<mm>[^\\s]+)\\s+(?P<yy>\\d+)", date, flags=re.I)
    if not searches:
        return date
    day = str(searches.group('dd'))
    if len(day) == 1:
        day = "0" + day
    month = months.index(searches.group('mm')) + 1
    if month < 10:
        month = "0" + str(month)
    year = str(searches.group('yy'))
    return str(day) + '/' + str(month) + '/' + year


def convert_list(data: list):
    dict = [{"date": convert_date(n[0]), "name": n[1]} for n in data]
    return dict


def write_csv(file_path: str, data):
    keys = data[0].keys()
    with open(file_path, 'w', newline='') as out_file:
        dict_writer = csv.DictWriter(out_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def write_json(txt_path: str, data):
    with open(txt_path, 'w') as fp:
        json.dump(data, fp, indent=4)
    return 1


def pretty_print(json_obj):
    json_formatted_str = json.dumps(json.loads(json.dumps(json_obj)), sort_keys=False, ensure_ascii=False, indent=4)
    print(json_formatted_str)


# zadanie 1
map_result = get_rnd_quotes(quote_qty)

sotrt_by_names = sorted(map_result, key=lambda n: n['Author'])
write_csv(csv_filename, sotrt_by_names)

# zadanie 2
converted = convert_list(read_txt_file(authors_path))
write_json(authors_json, converted)
