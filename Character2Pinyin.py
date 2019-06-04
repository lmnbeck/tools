#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pypinyin import pinyin, lazy_pinyin, Style
import sys
import linecache
import string
import re

CommandPinyinList=[]
CommandpinyinStr=''

file_reader = open("Keywords.txt",'r',encoding='utf-8') # 字符串报GBK错误，所以用encoding
file_writer = open('Keywords_pinyin.txt','w',encoding='utf-8')

# 读取一行
listoflines = file_reader.readline()
while listoflines:
    #print(listoflines)
    #print(listoflines.split(',')[1])

    # 分解字符串
    ID = listoflines.split(',')[0]
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
    CommandpinyinStr = ID + ', ' + CommandpinyinStr + ', ' + wordID
    #re.sub(r' ','sss',CommandpinyinStr)
    #print(type(CommandpinyinStr))
    #print(CommandpinyinStr)

    # 追加每一行到list,用于写入文件
    CommandPinyinList.append(CommandpinyinStr)
    #CommandPinyinList.append('\n')

    # 读取下一行
    listoflines = file_reader.readline()

args = sys.argv[:] 
print (args)

file_writer.writelines(CommandPinyinList)

# 关闭文件
file_reader.close()
file_writer.close()
