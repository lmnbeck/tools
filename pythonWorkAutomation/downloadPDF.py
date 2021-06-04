from selenium import webdriver
import time
import re

# setting chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")

# get url
browser = webdriver.Chrome(chrome_options = chrome_options)
url = 'http://www.cninfo.com.cn/new/disclosure/stock?stockCode=002594&orgId=gshk0001211#latestAnnouncement'
browser.get(url)
time.sleep(3)

# get page count by regular expression
data = browser.page_source
p_count = '<span class="total-box">共(.*?)条'
count = re.findall(p_count, data)[0]
print(count)
# pages = int(int(count)/30)
pages = 2

datas = []
datas.append(data)
for i in range(pages):	
	# simulate click [next] button by selenium
	browser.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div/div/div[2]/div[1]/div[3]/div/div/button[2]').click()
	time.sleep(3)
	data = browser.page_source
	datas.append(data)
	time.sleep(3)
alldata = ''.join(datas)

pdf_title = '<span class="r-title">(.*?)</span>'
pdf_address = '<a target="_blank" href="(.*?)".*?<span class="r-title"'
real_title = re.findall(pdf_title,alldata)
real_address = re.findall(pdf_address, alldata)

for i in range(len(real_title)):
	real_address[i] = re.sub("amp;","",real_address[i])
	real_address[i] = 'http://www.cninfo.com.cn' + real_address[i]
	#print(real_address[i])

	browser = webdriver.Chrome(chrome_options = chrome_options)
	browser.get(real_address[i])
	try:
		browser.find_element_by_xpath('//*[@id="noticeDetail"]/div/div[1]/div[3]/div[1]/button').click()
		time.sleep(3)
		browser.quit()
		print(str(i+1) + '.' + '下载完毕')
	except:
		print(real_title[i] + '没有pdf文件')