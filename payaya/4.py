import requests
import re
from bs4 import BeautifulSoup

url = "https://so.csdn.net/so/search/s.do"

p=1
s = 'python'
kv = {'p': '%d' % p, 'q': '%s' % s}
r = requests.get(url, params=kv)

r.encoding = 'utf-8'

so_url = r.request.url

html = r.text

print(requests.get(so_url).text)
