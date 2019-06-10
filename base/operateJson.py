import json

with open('../login.json', mode='r', encoding='utf-8') as fp:
    data = json.load(fp)
print(data['login'])
