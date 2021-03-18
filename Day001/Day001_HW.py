#作業目標
#1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
#檔案及API是檔案擁有者主動釋出，爬蟲是被動式釋出
#2.（實作）完成一個程式，需滿足下列需求：
from urllib.request import urlretrieve
import os
os.makedirs('./data',exist_ok=True) #exists_ok = true →如果該資料夾存在，不執行不會噴error
dirs = os.listdir('./data/')
files = []
for i in dirs:
    files.append(i)

if 'Homework.txt' in files:
    print('[O] , Homework.txt is exists!!')
else:
    print('[X] , Homework.txt isn\'t exists!!')

with open('./data/Homework.txt','w') as file:
    file.write('Hello World')

with open('./data/Homework.txt','r') as file2:
    data = file2.read()

if len('Hello world') == len(data):
    print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
else:
    print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')