import urllib
e="%E4%B8%AD%E6%96%87%E8%BD%AC"
print(urllib.parse.unquote(e))

str="咩"
print(urllib.parse.quote(e))