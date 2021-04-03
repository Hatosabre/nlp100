import re
import json
import os
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\03.regex" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

with open("data/uk_wiki.txt", "r", encoding="utf-8") as f:
    data = f.read()


re_texts = re.findall(r'^\{\{基礎情報.*?$(.*?)^\}\}', data, re.MULTILINE + re.DOTALL)

basic_dict = {}
for info in re_texts:
    kvs = re.findall(r'\|(.+?)\s*\=\s*(.+)', info)
    for kv in kvs:
        k = kv[0]
        v = kv[1]
        v = v.replace('（', '(')
        v = v.replace('）', ')')
        v = re.sub(r'\{\{(?:lang|仮リンク)(?:[^|]*?\|)*?([^|]*?)\}\}', r'\1', v)
        v = re.sub(r'\{\{(.+?)\}\}', '', v)   

        # 26
        v = re.sub(r'(\'{2,5})(.+?)(\1)', r'\2', v)

        # 27
        tmp = re.search(r'\[\[(.+?)(?:\|(.+?))*\]\]', v)
        if tmp:
            if tmp.group(2):
                v = re.sub(r'\[\[(.+?)(?:\|(.+?))*\]\]', r'\2', v)
            else:
                v = re.sub(r'\[\[(.+?)(?:\|(.+?))*\]\]', r'\1', v)

        v = re.sub(r'<.+?>(.*?)</.+?>', '', v)        
        v = re.sub(r'<.+?/>', '', v)     
        
        basic_dict[k] = v
        if k == "国旗画像":
            file_name = v
            break
    else:
        break

url_file = file_name.replace(' ', '_')

import requests

S = requests.Session()

URL = "https://commons.wikimedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop":"url",
    "titles": f"File:{url_file}"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA["query"]["pages"]["347935"]["imageinfo"][0]["url"])
