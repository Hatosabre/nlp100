import json
import os
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\03.regex" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

with open("data/jawiki-country.json", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data["title"] == "イギリス":
            uk_data = data["text"]

print(uk_data)

with open("data/uk_wiki.txt", "w", encoding="utf-8") as f:
    f.write(uk_data)