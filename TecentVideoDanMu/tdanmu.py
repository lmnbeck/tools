#-*- coding = uft-8 -*-
#@Time : 2020/9/26 4:35 下午
#@Author : 公众号 菜J学Python
#@File : tengxun_danmu-1.py

import requests
import json
import time
import pandas as pd

df = pd.DataFrame()
for page in range(15, 766, 30):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    url = 'https://mfm.video.qq.com/danmu?otype=json&callback=jQuery19103650923479592503_1616137522266&target_id=1264954440%26vid%3Ds0018wixg9h&session_key=1401%2C49%2C1616137524&timestamp=735&_=1616137522280'.format(page)

    print("正在提取第" + str(page) + "页")
    # json_str= 'jQuery19103650923479592503_1616137522266({"userId": "1", "id": "1", "title": "Meet with Lisa", "completed": "True"})'.strip('jQuery19103650923479592503_1616137522266(').strip(')')

    # print(json.loads(json_str))

    html = requests.get(url,headers = headers)
    print(html.text.strip('jQuery19103650923479592503_1616137522266(').strip(')'))
    bs = json.loads(html.text.strip('jQuery19103650923479592503_1616137522266(').strip(')'))  #strict参数解决部分内容json格式解析报错
    time.sleep(1)
    #遍历获取目标字段
    for i in bs['comments']:
        content = i['content']  #弹幕
        upcount = i['upcount']  #点赞数
        user_degree =i['uservip_degree'] #会员等级
        timepoint = i['timepoint']  #发布时间
        comment_id = i['commentid']  #弹幕id
        cache = pd.DataFrame({'弹幕':[content],'会员等级':[user_degree],
                              '发布时间':[timepoint],'弹幕点赞':[upcount],'弹幕id':[comment_id]})
        df = pd.concat([df,cache])
df.to_csv('tengxun_danmu.csv',encoding = 'utf-8')
print(df.shape)
