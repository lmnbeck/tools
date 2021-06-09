from selenium import webdriver
import re
import pandas as pd
import time


# setting chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")

# get url
browser = webdriver.Chrome(options = chrome_options)
url = 'http://zdscxx.moa.gov.cn:8080/nyb/pc/frequency.jsp'
browser.get(url)
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[2]/ul/li[1]').click()
time.sleep(2)
data = browser.page_source
table = pd.read_html(data)[0]

for i in range(1,6):
    browser.find_element_by_link_text ('下一页').click()
    time.sleep(2)
    data = browser.page_source
    table = table.append(pd.read_html(data)[0])
    print(table)

# table.to_excel("农产品价格.xlsx", index=False)