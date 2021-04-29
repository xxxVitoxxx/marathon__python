import requests
import json
'''
response = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers')
print(response.text)
'''
# 沒有加headers參數變成以下
'''
<html>
<head><title>403 Forbidden</title></head>
<body bgcolor="white">
<center><h1>403 Forbidden</h1></center>
<hr><center>openresty</center>
</body>
</html>
'''
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}
# 加上headers參數 user-agent才能成功發出請求

response = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers', headers=headers)
#print(response.text)

data = json.loads(response.text)
#print(data)
for d in data['data']:
    print(d)