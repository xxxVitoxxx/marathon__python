import requests
import json
response = requests.get('https://www.dcard.tw/_api/forums/job/posts?popular=true')
#print(response.text)
data = json.loads(response.text)
#print(data)
for i in data:
    print(i['title'])