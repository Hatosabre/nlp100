# 34. 名詞の連接Permalink
# # 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

import pandas as pd
import os
from tqdm import tqdm
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\04.morph_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

MECAB_NEKO_PATH = "data/neko.txt.mecab"
neko_mecab_df = pd.read_csv(MECAB_NEKO_PATH)


noun_clause_list = []

noun_clause_tmp = []
for row in tqdm(neko_mecab_df.iterrows(), total=len(neko_mecab_df)):
    pos = row[1]["pos"]
    surface = row[1]["surface"]

    ## 名詞が続く限り一時リストに保存
    ## 二つ以上保存されていれば、名詞節として登録
    ## 「あ「の」」のような「の」も名詞のため、違和感のある名詞節が出来る場合もある
    if pos == "名詞":
        noun_clause_tmp.append(surface)
    else:
        if len(noun_clause_tmp) > 1:
            noun_clause_list.append("".join(noun_clause_tmp))
            noun_clause_tmp.clear()

print(noun_clause_list)