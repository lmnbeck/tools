from pathlib import Path

while True:
    path2Find = input("where? ")
    path2Find = Path(path2Find.strip())
    if path2Find.exists() and path2Find.is_dir():
        break
    else:
        print('Please input a exist path!')

word2Find = input("find what? ").strip()

resultList = list(path2Find.rglob(f'*{word2Find}*'))
resultFile = []
resultFolder = []
if len(resultList) != 0:
    for i in resultList:
        if i.is_file():
            resultFile.append(i)
        elif i.is_dir():
            resultFolder.append(i)
else:
    print('no such file or folder!')

print('Folders:')
for i in resultFolder:
    print(i)
print('Files:')
for i in resultFile:
    print(i)