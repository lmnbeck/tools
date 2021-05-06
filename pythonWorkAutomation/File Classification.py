import os
import shutil

""" 把文件扩展名相同的文件移动到相同文件夹 """

src_folder = 'D:\\Software\\'
des_folder = 'D:\\Software\\after\\'
files = os.listdir(src_folder)

print(files)

for i in files:
    src_path = src_folder + i
    if os.path.isfile(src_path):
        des_path = des_folder + i.split('.')[-1]
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        shutil.move(src_path, des_path)


# appendexList = []
# for i in files:
#     src_path = src_folder + i
#     if not src_path.find('.') == -1:
#         appendex = src_path.split('.')[-1] + 'files'
#         des_path = des_folder + appendex 
        
#         if appendex not in appendexList:
#             if not os.path.exists(des_path):
#                 os.makedirs(des_path)
#             appendexList.append(appendex)
        
#         shutil.move(src_path, des_path)

