import requests
import json

url = "https://m.imooc.com/passport/user/login"
data = {
    "username": "17620016080",
    "password": "Ls06sRsjh6ibLVz8odNcNPOIswc76cHtHXsRflto+jwOTmOAKrOTrzVY6ECkyTBAvB8DQ2pbLwgGL0XoEJ7SQ85jxo845gkn1HIsHa2ck7yxzUicL7hnx2TR73nb8Bp6xk1u7xljGb6PNHfWHbg/L4qCQiT7s9BIVBR8gKte1MI=",
    "verify": "",
    "pwencode": "1",
    "referer": "https://m.imooc.com"
}

res = requests.post(url, data).json()
print(res)
