# coding: utf-8

import re
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
url = 'https://www.cnblogs.com/'
response = requests.get(url, headers = headers)
result = response.text
# print(result)

re_title = '<a class="post-item-title" href=".*?" target="_blank">(.*?)</a>'
titleList = re.findall(re_title, result)
for i in titleList:
	print(i)