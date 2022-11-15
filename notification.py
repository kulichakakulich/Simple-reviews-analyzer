from bs4 import BeautifulSoup
import requests
import time
import hashlib
from urllib.request import urlopen, Request
from requests_oauthlib import OAuth1Session

url = 'https://edu.21-school.ru/projects/code-review'

auth = 'https://edu.21-school.ru/'

page = requests.get(auth)
response = urlopen(auth).read()
print(response)
encode = 'utf-8'
dec = response.decode(encode)
f = open("pages.txt", "w")
f.write(dec)
f.close()

currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        response = urlopen(url).read()

        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()

        # wait for 30 seconds
        time.sleep(30)

        # perform the get request
        response = urlopen(url).read()

        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()

        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue
        else:
            print("something changed")
            response = urlopen(url).read()

    # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

    # wait for 30 seconds
            time.sleep(30)
            continue
    except Exception as e:
        print("error")