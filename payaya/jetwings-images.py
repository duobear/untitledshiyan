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
all_list_img=soup.select('img')

x=0
for book_one in all_list_img:
    img_src = book_one.get('src')
    img_alt = book_one.get('alt')


    # print("src="+img_src+"  alt="+img_alt)
    # last_src="http://1331682.s21i.faiusr.com/4/ABUIABAEGAAgmMrMkwUojsP4STD_CTiIAg.png"
    last_src="http:"+img_src
    request.urlretrieve(last_src, 'c:/python_spider_fild\%s.jpg' %img_alt)
    request.urlretrieve(last_src, 'c:/python_spider_fild\%s.png' %img_alt)
    # %x,%格式与前面的%对应，x对应的数字用字符串的形式表示




    #     x += 1

# x = 0
# for book_one in book_list_img:
#     book_img_url = book_one.get('src')
#     print(book_img_url)
#     request.urlretrieve(book_img_url, 'c:\python_spider_fild\%s.jpg' % x)
#     x += 1
