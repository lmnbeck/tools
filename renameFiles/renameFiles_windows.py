#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import tkinter
from tkinter import filedialog
import linecache
import string

def readFiles():
    # Open File by dialog
    openedFileList = filedialog.askopenfilenames(initialdir = 'D:')
    for file in openedFileList:
        print(file)
    return openedFileList

def changeName(openedFileList, originName):
    i = 0

    splitName = originName.split('.')
    for file in openedFileList:
        newName = splitName[0] + str(i) + '.' + splitName[1]
        print(newName)
        os.rename(file, newName)
        i = i+1

def main():
    newName = input()
    
    files = readFiles()
    changeName(files, newName)


if __name__ == "__main__":

    #file_reader = open(originalFile,'r',encoding='utf-8') # 字符串报GBK错误，所以用encoding
    #file_writer = open(outPutFile,'w',encoding='utf-8')  
    main()

