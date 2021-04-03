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
        
        # 1
        v = re.sub(r'\'{2,5}', '', v)
        
        basic_dict[k] = v
        print(v)

