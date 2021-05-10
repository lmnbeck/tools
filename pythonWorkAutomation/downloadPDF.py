from selenium import webdriver
import time
import re

browser = webdriver.Chrome()
url = 'http://www.cninfo.com.cn/new/disclosure/stock?stockCode=002594&orgId=gshk0001211#latestAnnouncement'
browser.get(url)
time.sleep(3)

