import urllib

from bs4 import BeautifulSoup#用于解析网页
import requests

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
url='https://image.baidu.com/'
r = requests.get(url,headers=headers)

bsObj = BeautifulSoup(r.text, 'html.parser')
t1 = bsObj.find_all('img')


def xx(a, b):
    pic_url = a
    pic_name = b
    with urllib.request.urlopen(pic_url, timeout=30) as response:
        if (response.status == 200):
             with urllib.request.urlopen(pic_url, timeout=30) as response, open('./rym/' + pic_name,'wb') as f:
                f.write(response.read())
                f.flush()
                f.close()
                print("成功")
        else:
            print(pic_url)


for t2 in t1:
    t3 = t2.get('src')
    urlj="https:"+t3
    print(urlj)
    name=t3.split('/')[-1]
    print(name)
    # xx(urlj,name)









