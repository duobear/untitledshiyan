#coding:utf-8
from collections import Counter
import requests
from bs4 import BeautifulSoup
from urllib import request
import urllib
url = 'http://zhaoyimedia.com/'

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}

r=requests.get(url,headers=headers)

# soup = BeautifulSoup(r.text.replace('<b>', '').replace('</b>', ''),'lxml')
soup=BeautifulSoup(r.text,'lxml')
url_list=soup.select('p')
for i in url_list:
    print(i.getText())