# 38.ヒストグラム
# # 単語の出現頻度のヒストグラムを描け．ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
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
axes[0].hist(neko_mecab_df["surface"].value_counts(), bins=int(neko_mecab_df["surface"].value_counts().max() // 10))

# 頻度(base)
axes[1].hist(neko_mecab_df["base"].value_counts(), bins=int(neko_mecab_df["base"].value_counts().max() // 10))

plt.show()
# ↑ よくある助詞や記号系が上位を占めてしまっている。

