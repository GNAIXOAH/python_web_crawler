import requests
url = "https://baidu.com"
r = requests.get(url)
r = requests.request("get", url)
print(r.status_code)
print(r.text)