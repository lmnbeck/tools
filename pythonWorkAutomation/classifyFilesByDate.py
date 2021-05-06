from pathlib import Path
from datetime import datetime
from exifread import process_file

scr_folder = Path('F:\\')
des_folder = Path('E:\\pic\\cameraCard\\')
if not des_folder.exists():
    des_folder.mkdir(parents = True)

file_list = list(scr_folder.glob('*.jpg'))
for i in file_list:
    with open(i.name) as f:
        dateInfo = process_file(f, details = False)
    if 'EXIF DateTimeOriginal' in dateInfo.keys():
        des_folder_name = dateInfo['EXIF DateTimeOriginal'] 
    des_folder = des_folder / des_folder_name
    if not des_folder.exists():
        des_folder.mkdir(parents = True)
    i.replace(des_folder)
