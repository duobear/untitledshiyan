import requests
import re
from bs4 import BeautifulSoup
url="https://www.baidu.com/"
kv={'wd':"hah"}
r = requests.get(url, params=kv)
r.encoding='utf-8'
print(r.encoding)

soup=BeautifulSoup(r.text,"html.parser")
print (soup.title)
print((soup.text))