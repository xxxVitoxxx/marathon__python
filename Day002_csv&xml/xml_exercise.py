### xml.dom.mindom
print('{0:-^30s}'.format('xml.dom.mindom'))
import xml.dom.minidom
# 存取檔案
doc = xml.dom.minidom.parse('./data/Day002.xml')

# 抬頭
print(doc.getElementsByTagName('Title')[0].firstChild.nodeValue)

# 抓name名稱 ＆ 文字
chapters = doc.getElementsByTagName('Chapter')

for chapter in chapters:
    print('name:{} , text:{}'.format(chapter.getAttribute('name'),chapter.firstChild.nodeValue))


### xml.etree.ElementTree
print('{0:-^30s}'.format('xml.etree.ElementTree'))
import xml.etree.ElementTree as ET
# 存取檔案
tree = ET.parse('./data/Day002.xml')
root = tree.getroot()

# 抬頭
print(root[0].text)

# 抓name名稱 ＆ 文字
chapters = root[2]
for chapter in chapters:
    print('name:{} , text:{}'.format(chapter.attrib['name'],chapter.text))

### xmltodict
print('{0:-^30s}'.format('xmltodict'))
import xmltodict
# 存取檔案
with open('./data/Day002.xml') as fd:
    doc = dict(xmltodict.parse(fd.read()))
print(doc)
# 抬頭
print(doc['CUPOY']['Title'])

# 抓name名稱 ＆ 文字
chapters = doc['CUPOY']['Chapters']['Chapter']

for chapter in chapters:
    print('name:{} , text:{}'.format(chapter['@name'],chapter['#text']))