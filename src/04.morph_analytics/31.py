# 31. 動詞Permalink
# # 動詞の表層形をすべて抽出せよ．

import pandas as pd
import os
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\04.morph_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

MECAB_NEKO_PATH = "data/neko.txt.mecab"
neko_mecab_df = pd.read_csv(MECAB_NEKO_PATH)

# pos == "動詞"の 表層系(=surface)に絞り込み
print(neko_mecab_df[neko_mecab_df["pos"] == "動詞"]["surface"].value_counts(ascending=False))

