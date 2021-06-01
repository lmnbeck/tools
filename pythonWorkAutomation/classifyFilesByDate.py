from pathlib import Path
from datetime import datetime
from exifread import process_file

""" 按照日期分类照片 """

# scr_folder = Path('F:\\')
scr_folder = Path('E:\\pic\\cameraCard\\')
des_folder = Path('E:\\pic\\cameraCard\\')
if not des_folder.exists():
    des_folder.mkdir(parents = True)

file_list = list(scr_folder.glob('*.jpg'))
for i in file_list:
    with open(i, 'rb') as f:
        dateInfo = process_file(f, details = False)
    if 'EXIF DateTimeOriginal' in dateInfo.keys():
        dto = str(dateInfo['EXIF DateTimeOriginal'] )
        des_folder_name = datetime.strptime(dto, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')
        des_path = des_folder / des_folder_name
    if not des_path.exists():
        des_path.mkdir(parents = True)
    i.replace(des_path / i.name)
