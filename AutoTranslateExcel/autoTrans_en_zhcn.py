
import xlwings as xw
from google_trans_new import google_translator

def translateCell(text, lang):
    translator = google_translator(timeout=10)
    translations = translator.translate(text, lang)
    print("翻译结果:", translations)
    return translations


# 打开Excel程序，默认设置：程序可见，只打开不新建工作薄，屏幕更新关闭
app = xw.App(visible=False, add_book=False)
try:
    wb = app.books.open(r'E:\05_Development\FunctionSafety\DFEMA\System Dfmea.xlsx')
    # 读取所有sheet
    x = []
    num = len(wb.sheets)
    for i in range(0, num):
        sht = wb.sheets[i]
        x.append(sht)
    
    data = sht.range('A10').expand().value

    # for line in data:
    for cell in data:
        if isinstance(cell, float):
            continue
        textEN = translateCell(cell, 'zh-CN')
        cell = str(cell) + '\n' + textEN

    # text = wb.sheets['sheet1'].range(1,1).value
    # print(text)

    # textEN = translateCell(text, 'zh-CN')

    # wb.sheets['sheet1'].range(1,1).value = text + '\n' + textEN

    wb.save(r'E:\05_Development\FunctionSafety\DFEMA\test_translated.xlsx')
    wb.close()
except Exception as e:
    print(e)
finally:
    app.quit()
