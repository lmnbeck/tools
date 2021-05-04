from pathlib import Path
from PIL import Image

scr_folder = Path('/home/ubuntu/workSpace/pic/before/')
des_folder = Path('/home/ubuntu/workSpace/pic/after/')
if not des_folder.exists():
    des_folder.mkdir(parents = True)

file_list = list(scr_folder.glob('*.jpg'))
for i in file_list:
    des_file = des_folder / i.name
    des_file = des_file.with_suffix(".PNG")
    Image.open(i).save(des_file)
    print("%s finished type chang " % i.name)


