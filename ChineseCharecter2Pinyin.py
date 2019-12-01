#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pypinyin import pinyin, lazy_pinyin, Style
from tkinter import filedialog
import linecache
import string

def ChineseCaracter2Pinyin():
    # Open File by dialog
    originalFile = filedialog.askopenfilename(initialdir = 'D:')
    print(originalFile)
    
    outPutFile = originalFile.split(".")[0]+"_pinyin"+".txt"
    print(outPutFile)
    file_reader = open(originalFile,'r') # 字符串报GBK错误，所以用encoding
    file_writer = open(outPutFile,'w')

    # 读一行
    oneLine = file_reader.readline()

    # 转Pinyin并写文件
    while(oneLine):
 

        # 把汉字转为拼音
        Commandpinyin = pinyin(oneLine,style=Style.TONE3)
        
        # 数字无法直接join，所以用s%
        CommandpinyinStr = " ".join('%s' %id for id in Commandpinyin)
        print(CommandpinyinStr)

        # 删除无用字符
        CommandpinyinStr = CommandpinyinStr.replace('[','')
        CommandpinyinStr = CommandpinyinStr.replace("]",'')
        CommandpinyinStr = CommandpinyinStr.replace("\'",'')
        CommandpinyinStr = CommandpinyinStr.replace("\\n",'')
        CommandpinyinStr = CommandpinyinStr.strip()
        #CommandpinyinStr = ID + ',' + CommandpinyinStr + ',' + '1' + '\n'
        
        file_writer.writelines(CommandpinyinStr)
        file_writer.writelines("\n")
        
        # 读取下一行
        oneLine = file_reader.readline()
    
    # 关闭文件
    file_reader.close()
    file_writer.close()
    

if __name__ == "__main__":

    #file_reader = open(originalFile,'r',encoding='utf-8') # 字符串报GBK错误，所以用encoding
    #file_writer = open(outPutFile,'w',encoding='utf-8')  
    ChineseCaracter2Pinyin()

