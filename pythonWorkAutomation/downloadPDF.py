from selenium import webdriver
import time
import re


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")

browser = webdriver.Chrome(chrome_options = chrome_options)
url = 'http://www.cninfo.com.cn/new/disclosure/stock?stockCode=002594&orgId=gshk0001211#latestAnnouncement'
browser.get(url)
time.sleep(3)

#   WARNING: The scripts pip, pip3 and pip3.8 are installed in '/home/ubuntu/.local/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.