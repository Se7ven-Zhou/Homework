#coding:utf-8

import requests
req = requests.get("http://httpbin.org/get")

print(req.url)
print(req.text)