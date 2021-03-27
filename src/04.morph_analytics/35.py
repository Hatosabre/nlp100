# 35. 単語の出現頻度Permalink
# # 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

import pandas as pd
import os
from tqdm import tqdm
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\04.morph_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

MECAB_NEKO_PATH = "data/neko.txt.mecab"
neko_mecab_df = pd.read_csv(MECAB_NEKO_PATH)

# 頻度(surface)
print(neko_mecab_df["surface"].value_counts(ascending=False))

# 頻度(base)
print(neko_mecab_df["base"].value_counts(ascending=False))