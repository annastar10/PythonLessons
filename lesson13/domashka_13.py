import csv
import json
import re
import requests
from os import path
from random import randint
from time import sleep

quote_qty = 5
csv_filename = os.path.abspath('quotes.csv')
authors_path = os.path.abspath('authors.txt')

url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&jsonp=parseQuote"
json_filename = os.path.abspath('authors.json')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']


def getRandomQuotes(qty: int):
    quotes = []
    unique_quotes = []
    safe_count = qty * 4  # safe  interval to get out from eternal while loop
    while len(quotes) <= qty - 1 and safe_count > 1:
        response = requests.request("GET", url, headers={}, data={})
        if not response.status_code == 200:
            safe_count -= 1
            continue
        resp = json.loads(response.text)
        author = resp.get("quoteAuthor")
        quote = resp.get("quoteText")
        quote_url = resp.get("quoteLink")
        if any(quote in s for s in unique_quotes):
            safe_count -= 1
            continue
        if author == '' or quote == '' or quote_url == '':
            safe_count -= 1
            continue
        quotes.append({"Author": author, "Quote": quote, "URL": quote_url})
        unique_quotes.append(quote)
        # чтобы не нагружать ресурс сделаем паузу
        sleep(randint(1, 4))
    return quotes


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


def write_file(path: str, data):
    fname, file_ext = os.path.splitext(path)
    if file_ext == '.csv':
        keys = data[0].keys()
        with open(path, 'w', newline='') as out_file:
            dict_writer = csv.DictWriter(out_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    elif file_ext == '.txt':
        return open(path, "w").write(data)
    elif file_ext == '.json':
        with open(path, 'w') as fp:
            json.dump(data, fp, indent=4)


# zadanie 1
map_result = getRandomQuotes(quote_qty)

if len(map_result) == quote_qty:
    sotrt_by_names = sorted(map_result, key=lambda n: n['Author'])
    # не смогу сделать имя файла по умолчанию в функции так как она записывает и json файл
    write_file(csv_filename, sotrt_by_names)
else:
    print("Wrong amount of quotes \n", "Requested amount is: " + str(quote_qty) + "\n",
          "I've got: " + str(len(map_result)))

# zadanie 2
converted = convert_list(read_txt_file(authors_path))
write_file(json_filename, converted)
