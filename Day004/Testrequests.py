import requests

response = requests.get('https://github.com/timeline.json')
print(response.text)