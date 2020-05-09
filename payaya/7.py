import os
import urllib

import requests
import re
from bs4 import BeautifulSoup

url = "https://so.csdn.net/so/search/s.do"

p=1
s = 'python'
kv = {'p': '%d' % p, 'q': '%s' % s}
r = requests.get(url, params=kv)
r.encoding = 'utf-8'
soup=BeautifulSoup(r.text,"html.parser")
print(soup.img['src'])
URL=soup.img['src']
if not os.path.exists("./rym"):
    print("不纯在")
    os.makedirs("./rym")

else:
    print("存在")


    with urllib.request.urlopen( URL, timeout=30) as response, open("./rym/lyj.png", 'wb') as f_save:
        f_save.write(response.read())
        f_save.flush()
        f_save.close()
        print("成功")




