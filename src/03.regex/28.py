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
        print(k, v)

