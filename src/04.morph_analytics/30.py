# 30. 形態素解析結果の読み込みPermalink
# # 形態素解析結果（neko.txt.mecab）
# # を読み込むプログラムを実装せよ．
# # ただし，各形態素は
# # 表層形（surface），
# # 基本形（base），
# # 品詞（pos），
# # 品詞細分類1（pos1）
# # をキーとするマッピング型に格納し，
# # 1文を形態素（マッピング型）のリストとして表現せよ．
# # 第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import os
import pandas as pd
import MeCab

ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\04.morph_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)
from common import load_neko

NEOLOGD_PATH = r"/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd" # >> 自身の環境に合わせる
m = MeCab.Tagger(f"-d {NEOLOGD_PATH}")

FILE_PATH = "data/neko.txt"
neko_data = load_neko(FILE_PATH)

mecab_result = []
for line in neko_data:

    # 分かち書き
    parse_results = m.parse(line)
    parse_result_list = parse_results.split("\n")
    for parse_result in parse_result_list:
        if parse_result == "EOS":
          break
        result_infos = parse_result.split("\t")

        # 表層
        surface = result_infos[0]

        # 単語情報
        result_pos = result_infos[1].split(",")
        pos = result_pos[0]
        pos1 = result_pos[1]
        base = result_pos[6]

        mecab_result.append([
            surface,
            pos,
            pos1,
            base
        ])

## 各形態素は
## 表層形（surface），
## 基本形（base），
## 品詞（pos），
## 品詞細分類1（pos1）
## をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ
## {[surface, base, pos, pos1]: ?}
## ↑理解できない。一旦Pandasに保存
mecab_df = pd.DataFrame(mecab_result, columns=["surface", "pos", "pos1", "base"])

# CSVで保存
mecab_df.to_csv("data/neko.txt.mecab", index=False)