from pathlib import Path
from filecmp import cmp

#  Define the folders to compare
src_folder = Path(input("where?").strip())
des_folder = Path(input("To where?").strip())
if not des_folder.exists():
    des_folder.mkdir(parents=True)

#  list up all the files
srcFiles = list(src_folder.rglob('*'))

# Judge if it is a file,to reduce the for loop rounds
file_list = []
for i in srcFiles:
    if i.is_file():
        file_list.append(i) 

for m in srcFiles:
    for n in srcFiles:
        #  find the same file name in list
        if m != n and m.exists() and n.exists():
            if cmp(m,n):
                print(n, " has same file as ", m)
                #  move the same file to des_folder
                n.replace(des_folder / n.name)
                print("move ",n ,"to ",des_folder)
