#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

url = "https://so.csdn.net/so/search/s.do"
p = 0
# s = input()
s = 'python'
for p in range(10):
    p = p + 1

kv = {'p': '%d' % p, 'q': '%s' % s}

r = requests.get(url, params=kv)

print(r.encoding)
# htmlCharset = "utf-8"


soup = BeautifulSoup(r.text, "html.parser",from_encoding='utf-8')


print (soup.title)






for dl in soup.find_all('dl'):
    text = dl.prettify()


# search_url = dl.get('data-track-view')
#
# search = re.findall(r'"con":"(.*?)"', search_url)[0]
#
# content = requests.get(search).text

# print(content)

# tittle = re.findall(r'<div class="limit_width">\n.*?<a.*?>(.*?)</a>\n.*?<a', text, re.S)[0]
#
# tittle = tittle.replace('<em>', '')
#
# tittle = tittle.replace('</em>', '')
#
# tittle = tittle.replace(' ', '')
#
# tittle = tittle.replace('\n', '')
#
# fb = open('%s.html' % tittle, 'w', encoding='utf-8')
#
# fb.write(content)
#
# print(search, tittle)
