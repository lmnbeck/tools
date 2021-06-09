# coding: utf-8

import re
import requests
import pandas as pd

def paByPage(page):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
	url = 'http://bang.dangdang.com/books/bestsellers/1-' + str(page) 
	response = requests.get(url, headers = headers)
	result = response.text
	# print(result)

	r_title = '<a href=".*?" target="_blank" title="(.*?)">.*?</a>'
	r_rank = '<div class="list_num.*?">(\d*).</div>'
	r_price_n = '<div class="price">.*?<span class="price_n">&yen;(.*?)</span>'
	r_price_r = '<div class="price">.*?<span class="price_r">&yen;(.*?)</span>'
	titles = re.findall(r_title, result)
	# print(titles)
	ranks = re.findall(r_rank, result)
	# print(ranks)
	price_n = re.findall(r_price_n, result, re.S)
	price_r = re.findall(r_price_r, result, re.S)
	# print(price_n)
	# print(price_r)

	data = {'rank': ranks, 'title': titles, 'price': price_r, 'price_discount': price_n}
	data = pd.DataFrame(data)
	# print(data)
	# data.to_excel('当当图书销量排行榜.xlsx', index=False)
	return data

all_data = pd.DataFrame()
for i in range(1,6):
	all_data = all_data.append(paByPage(page))
all_data.to_excel('当当图书销量排行榜.xlsx', index=False)