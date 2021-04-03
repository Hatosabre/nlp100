import re
import json
import os
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\03.regex" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

with open("data/uk_wiki.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

for d in data:
    check = re.match(r'\[\[Category:(.+?)(\|.+)*\]\]', d)
    if check:
        print("========")
        print(d)