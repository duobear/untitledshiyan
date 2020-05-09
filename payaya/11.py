# coding=utf-8
import urllib.request
import time

# 在请求加上头信息，伪装成浏览器访问
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
chaper_url = 'http://baidu.com'

vist_num = 1
while vist_num < 10:
    if vist_num % 50 == 0:
        time.sleep(5)
    print("This is the 【 " + str(vist_num) + " 】次尝试")
    req = urllib.request.Request(url=chaper_url, headers=headers)
    urllib.request.urlopen(req).read()  # .decode('utf-8')
    vist_num += 1