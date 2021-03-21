from urllib.request import urlretrieve
import os , sys , chardet
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./1.txt")
urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./data/Homework.txt")
dirs = os.listdir('./')
for f in dirs:
    print(f)

a = open('./data/Homework.txt','r')
f = a.read()
print(f)
print(chardet.detect(f))
