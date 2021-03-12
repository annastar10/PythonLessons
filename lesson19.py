import requests
from requests_oauthlib import OAuth1

auth = OAuth1("f9a38f3a37ea4c9b8f7db07e9c93bfd4", "54d2982e1e2942acb92515a844e3db26")
endpoint = "http://api.thenounproject.com/icon/1"

response = requests.get(endpoint, auth=auth)
response_json = response.json()
print (response_json)