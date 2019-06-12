#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pypinyin import pinyin, lazy_pinyin, Style
import sys
import linecache
import string
import re

CommandPinyinList=[]
CommandpinyinStr=''
lines = 1

#CommandPinyinList.append('# event, text, flg\n')

file_reader = open("record_text.txt",'r',encoding='utf-8') # 字符串报GBK错误，所以用encoding
file_writer = open('Keywords_pinyin.txt','w',encoding='utf-8')
funWriter = open('dic_set_func.txt','w',encoding='utf-8')
trigWriter = open('dic_set_trig.txt','w',encoding='utf-8')

# 读取第二行
listoflines = file_reader.readline()
listoflines = file_reader.readline()
while listoflines:
    #print(listoflines)
    #print(listoflines.split(',')[1])

    # 分解字符串
    ID = listoflines.split(',')[0]
    ID = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", ID) # 去掉数字前面的0
    text = listoflines.split(',')[1]
    wordID = listoflines.split(',')[2]
    
    # 把汉字转为拼音
    Commandpinyin = pinyin(text,style=Style.TONE3)
    print(Commandpinyin)
    #print(type(Commandpinyin))

    # 数字无法直接join，所以用s%
    CommandpinyinStr = " ".join('%s' %id for id in Commandpinyin)
    print(CommandpinyinStr)

    # 删除无用字符
    CommandpinyinStr = CommandpinyinStr.replace('[','')
    CommandpinyinStr = CommandpinyinStr.replace("]",'')
    CommandpinyinStr = CommandpinyinStr.replace("\'",'')
    CommandpinyinStr = ID + ',' + CommandpinyinStr + ',' + '1' + '\n'
    #re.sub(r' ','sss',CommandpinyinStr)
    #print(type(CommandpinyinStr))
    #print(CommandpinyinStr)

    # 追加每一行到list,用于写入文件
    CommandPinyinList.append(CommandpinyinStr)
    #CommandPinyinList.append('\n')

    # 读取下一行
    listoflines = file_reader.readline()
    lines = lines + 1

args = sys.argv[:] 
print (args)

file_writer.writelines(CommandPinyinList)

#写dic_set_func.txt
funWriter.writelines("#keyword_id,a_threshold,sil_discount,waiting_time\n")
for i in range(1,lines):
    dic_set_fun = str(i) + ",500,1000,100\n"
    funWriter.writelines(dic_set_fun)

#写dic_set_trig.txt
trigWriter.writelines("#keyword_id, a_threshold, sil_discount, waiting_time\n")
trigWriter.writelines("1,500,1000,100")


# 关闭文件
file_reader.close()
file_writer.close()
funWriter.close()
trigWriter.close()
