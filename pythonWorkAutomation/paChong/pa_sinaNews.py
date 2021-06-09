from selenium import webdriver
import re
import pandas as pd

def x_news(x_words):
	# setting chrome
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument("window-size=1024,768")
	chrome_options.add_argument("--no-sandbox")

	# get url
	browser = webdriver.Chrome(options = chrome_options)
	url = 'http://search.sina.com.cn/?q=' + x_words + '&c=news&sort=time'
	browser.get(url)

	data = browser.page_source
	# print(data)
	browser.quit()

	r_href = '<div class="box-result clearfix".*?<a href="(.*?)" target="_blank">.*?</a>'
	r_title = '<div class="box-result clearfix".*?<a href=".*?" target="_blank">(.*?)</a>'
	r_date = '<span class="fgray_time">(.*?)</span>'

	hrefs = re.findall(r_href, data, re.S)
	titles = re.findall(r_title, data, re.S)
	dates = re.findall(r_date, data)
	print(len(hrefs), len(titles), len(dates))

	for i in range(len(hrefs)):
		titles[i] = re.sub('<.*?>', '', titles[i])

		dates[i] = dates[i].split(' ')[1]
		# print(f'{i+1}.{titles[i]} | {dates[i]}')
		# print(hrefs[i])

	data = pd.DataFrame({'标题': titles, '日期': dates, '链接': hrefs})
	print(data)
	# data.to_excel(x_words + '新浪新闻.xlsx', index=False)


x_news('比亚迪')