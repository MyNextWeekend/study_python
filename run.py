import requests

headers = {
    "cookie": "SESSDATA=ccb9baca%2C1698058515%2C5db18%2A42;"
}

a = requests.get("https://api.bilibili.com/x/web-interface/nav", headers=headers)
print(a.text)

b = requests.get("https://api.bilibili.com/x/web-interface/newlist?rid=231&type=0&ps=30&pn=1", headers=headers)
for i in b.json().get("data").get("archives"):
    print(i)
