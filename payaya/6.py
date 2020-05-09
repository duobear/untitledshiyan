import re

import requests
import lxml
from bs4 import BeautifulSoup

kv={"wd":"hah"}
url = 'http://www.baidu.com'

# page=urllib2.urlopen(url)

r = requests.get(url, params=kv)
r.encoding="utf-8"
page = r.text

print(r.encoding)
pagesoup = BeautifulSoup(page, 'lxml')
for link in pagesoup.find_all(name='a', attrs={"href": re.compile(r'^http:')}):
    # 找出所有a标签中的href属性中包含http的内容，这就是我们要找的网页的一级链接（ 这里不做深度遍历链接）
    # print(link.get_text())
    print(link.text)
    f=open('book.txt',"a+",encoding="utf-8")
    f.write(link.text)
f=open('book.txt',"a+",encoding="utf-8")
f.write("====================\n\n")