# coding: utf-8

from selenium import webdriver
import time

# setting chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")

# get url
browser = webdriver.Chrome(chrome_options = chrome_options)
url = 'https://www.baidu.com/'
browser.get(url)
time.sleep(3)

# xpath法
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
browser.find_element_by_xpath('//*[@id="su"]').click()

# css_selector法
browser.find_element_by_css_selector('#kw').send_keys('python')
browser.find_element_by_css_selector('#su').click()
