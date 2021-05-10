from selenium import webdriver
import time
import re

browser = webdriver.Chrome()
url = 'http://www.cninfo.com.cn/new/disclosure/stock?stockCode=002594&orgId=gshk0001211#latestAnnouncement'
browser.get(url)
time.sleep(3)

#   WARNING: The scripts pip, pip3 and pip3.8 are installed in '/home/ubuntu/.local/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.