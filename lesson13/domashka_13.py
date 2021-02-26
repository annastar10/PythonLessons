import json
import requests
import time

url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&jsonp=parseQuote"


def getRandomQuotes(qty: int):
    quotes = []
    save_count = qty * 2
    while len(quotes) <= qty:
        response = requests.request("GET", url, headers={}, data={})
        if response.status_code == 200:
            resp = json.loads(response.text)
            author = resp['quoteAuthor']
            if not author == '':
                quotes.append(resp)
        time.sleep(2)
        save_count -= 1
        if save_count < 1:
            break
    return quotes


map_result = getRandomQuotes(4)

print(map_result)
