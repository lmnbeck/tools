import sys
import linecache
import re

inputResultFile = sys.argv[1]

fresult = open(inputResultFile,'r')
fkeywordtrig = "D:\workSpace\OJT\Test_data\labels\keywords.zhCN.midea_cooker03_trig.txt"
fkeywordfunc = "D:\workSpace\OJT\Test_data\labels\keywords.zhCN.midea_cooker03_func.txt"
fkeywordtime = "D:\workSpace\OJT\Test_data\labels\keywords.zhCN.midea_cooker03_time.txt"
fmlf = open(r"D:\workSpace\OJT\Test_data\labels\uttID_text_label.mlf",'r')

fkeyword = fkeywordtrig
wavName = ""
RealCommand = ""
RecognizedCMD =""
keyword_line_number = -1
keyword_Detected = False
TriggerModeFlag = False

N = 215.0
Ctrig = 0.0
Ccmd = 0.0
Rtrig = 0.0
Rcmd = 0.0

# 解析result文件内容
line =fresult.readline()
while line:
    #print(line)
    #按行解析result文件
    if line.find("trig-") != -1:
        print(line)
        fkeyword = fkeywordtrig
    elif line.find("func-") != -1:
        print(line)
        fkeyword = fkeywordfunc
    elif line.find("time-") != -1:
        print(line)
        fkeyword = fkeywordtime

    #读取WAV文件名
    if line.find(".wav") != -1:
        wavName = line[-14:-5]
        print(wavName)
        RealCommand = ""
    else:
        wavName = "notFound"

    #读取识别到的keyword号码
    pos_foundKeyword = line.find("detected keyword") 
    if pos_foundKeyword != -1 and keyword_Detected == False:
        keyword_index = pos_foundKeyword + 16
        keyword_line_number = int(line[keyword_index:keyword_index+3].strip())+1
        print("keyword_line_number: ",keyword_line_number)
        keyword_Detected = True
        #print("keyword_Detected: ",keyword_Detected)
        if TriggerModeFlag == True:
            Rtrig = Rtrig+1
        else:
            Rcmd = Rcmd+1
        print("N,Rtrig,Rcmd,Ctrig,Ccmd")
        print(N,Rtrig,Rcmd,Ctrig,Ccmd)
    else:
        keyword_line_number = -1

    #清空keyword_Detected flag
    if line.find('mode') != -1:
        keyword_Detected = False
        #print("keyword_Detected: ",keyword_Detected)
        if line.find('trigger') != -1:
            TriggerModeFlag = True
        elif line.find('command') != -1:
            TriggerModeFlag = False

    #解析mlf文件内容
    linemlf = fmlf.readline()
    while linemlf:
        if linemlf.find(wavName) != -1:
            pos_realCommand = linemlf.rfind('\t')
            RealCommand = linemlf[(pos_realCommand+1):]
            print("RealCommand is:",RealCommand)
            break
        #下一行mlf文件的读取
        linemlf = fmlf.readline()
    #文件指针返回文件头
    fmlf.seek(0)

    #解析keyword文件内容
    if keyword_line_number> 0:   
        RecognizedCMD = linecache.getline(fkeyword,keyword_line_number)
        RecognizedCMD = re.sub(r'([\d]+)','',RecognizedCMD)
        print("RecognizedCMD is:",RecognizedCMD)

    if RealCommand == RecognizedCMD and RecognizedCMD != "":
        RecognizedCMD =""
        print("Recognized!!!")
        if TriggerModeFlag == True:
            Ctrig = Ctrig+1
        else:
            Ccmd = Ccmd+1
        print("N,Rtrig,Rcmd,Ctrig,Ccmd")
        print(N,Rtrig/215,Rcmd/215,Ctrig/215,Ccmd/215)
    
    #下一行result文件的读取
    line = fresult.readline()


fresult.close()
fmlf.close()
