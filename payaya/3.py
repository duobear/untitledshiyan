import requests
import re
from bs4 import BeautifulSoup

url = "https://so.csdn.net/so/search/s.do"

for p in range(10):
    p = p + 1
    s = 'python'
    kv = {'p': '%d' % p, 'q': '%s' % s}


    print(kv)
r = requests.get(url, params=kv)
print(r.url)
    # {'p': '1', 'q': 'python'}
    # {'p': '2', 'q': 'python'}
    # {'p': '3', 'q': 'python'}
    # {'p': '4', 'q': 'python'}
    # {'p': '5', 'q': 'python'}
    # {'p': '6', 'q': 'python'}
    # {'p': '7', 'q': 'python'}
    # {'p': '8', 'q': 'python'}
    # {'p': '9', 'q': 'python'}
    # {'p': '10', 'q': 'python'}
    # https://python.csdn.net
