#! /usr/env/python3

import requests
from bs4 import BeautifulSoup as bs

textAsList = []

req = requests.get('http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')

if req.status_code == 200:
    content = req.content
    website = bs(content, 'html.parser')
    for i in range(218, 310):
        text = website.findAll('p', {'data-reactid':i})
        textAsList.append(str(text)[23:-5])
        

for item in textAsList:
    print(item)