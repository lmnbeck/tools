
from tkinter.tix import COLUMN
import xlwings as xw
from google_trans_new import google_translator
import time

def translateCell(text, lang):
    translator = google_translator(timeout=10)
    if (text == "TBD" or text == "NA"):
        translations = ""
    else:
        translations = translator.translate(text, lang)
        print("翻译结果:", translations)
    
    return translations

Tstart = time.perf_counter()

# 打开Excel程序，默认设置：程序可见，只打开不新建工作薄，屏幕更新关闭
app = xw.App(visible=False, add_book=False)
try:
    wb = app.books.open(r'E:\05_Development\FunctionSafety\DFEMA\System Dfmea.xlsx')
    # 读取所有sheet
    #x = []
    num = len(wb.sheets)
    print("num of sheets: ", num)

    for i in range(0, num):
        sht = wb.sheets[i]
        #x.append(sht)

        rows = sht.used_range.last_cell.row
        columns = sht.used_range.last_cell.column
        ranges = "A" + str(10) + ":AA" + str(rows)
        data = sht.range(ranges).value

        # for line in data:
        rowNumber = 10
        for line in data:
            columnNumber = 1
            for cell in line:
                if (isinstance(cell, float) or cell is None):
                    columnNumber += 1
                    continue
                textzhCN = translateCell(cell, 'zh-CN')
                cell = str(cell) + '\n' + textzhCN
                # print(cell)
                wb.sheets[sht].range(rowNumber,columnNumber).value = cell
                columnNumber += 1
            rowNumber += 1
        
        wb.save(r'E:\05_Development\FunctionSafety\DFEMA\test_translated.xlsx')

    Tend = time.perf_counter()
    print('程序运行时间:%s毫秒' % ((Tend - Tstart)*1000))

    # text = wb.sheets['sheet1'].range(1,1).value
    # print(text)

    # textzhCN = translateCell(text, 'zh-CN')

    # wb.sheets['sheet1'].range(1,1).value = text + '\n' + textzhCN

    # wb.save(r'E:\05_Development\FunctionSafety\DFEMA\test_translated.xlsx')
    # wb.close()
except Exception as e:
    print(e)
finally:
    wb.close()
    app.quit()
