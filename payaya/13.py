# coding=utf-8
import urllib.request
import re


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1
        print(str(x))


html = getHtml("http://image.baidu.com/channel?c=%E6%91%84%E5%BD%B1&t=%E5%85%A8%E9%83%A8&s=0")

print(getImg(html))