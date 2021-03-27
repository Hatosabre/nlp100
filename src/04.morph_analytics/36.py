# 36. 頻度上位10語
# # 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

import pandas as pd
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\04.morph_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

MECAB_NEKO_PATH = "data/neko.txt.mecab"
neko_mecab_df = pd.read_csv(MECAB_NEKO_PATH)


fig, axes = plt.subplots(1, 2, figsize=(20, 10))
# 頻度(surface)
neko_mecab_df["surface"].value_counts(ascending=False).head(10).plot(kind="barh", ax=axes[0])

# 頻度(base)
neko_mecab_df["base"].value_counts(ascending=False).head(10).plot(kind="barh", ax=axes[1])

plt.show()
# ↑ よくある助詞や記号系が上位を占めてしまっている。

