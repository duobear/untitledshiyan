import requests
import re
from bs4 import BeautifulSoup

url = "https://so.csdn.net/so/search/s.do"


r = requests.get(url)


print(r.headers)

print(r.url)
print(r.origin)
