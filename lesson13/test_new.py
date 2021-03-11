import requests

url = "http://api.forismatic.com/api/1.0/"

for number in range(1, 20):
    params = {"method": "getQuote",
              "format": "json",
              "key": number,
              "lang": "ru"}
    responce = requests.get(url, params=params)
    result = responce.json()
    for key in result:
        print(f"{key} ------ {result[key]}")