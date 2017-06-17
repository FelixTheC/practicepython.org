#! /usr/env/python3
import requests
from bs4 import BeautifulSoup as bs

titles = []
links = []
realLinks = []
req = requests.get('https://www.nytimes.com/')
content = req.content
website = bs(content, 'html.parser')
headings = website.find_all('h2', 
                            {'class':'story-heading'}
                            )

for item in headings:
    linkRaw = str(item.find('a'))
    to = linkRaw.find('>')
    links.append(linkRaw[9:to-1])
    titles.append(item.text)
    
    
print(links[0] +' - '+ titles[0])
