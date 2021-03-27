# 37. 「猫」と共起頻度の高い上位10語Permalink
# # 「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

import pandas as pd
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
from collections import Counter
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\04.morph_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

MECAB_NEKO_PATH = "data/neko.txt.mecab"
neko_mecab_df = pd.read_csv(MECAB_NEKO_PATH)

neko_index = neko_mecab_df[neko_mecab_df["surface"] == "猫"].index.tolist()

occur_neko_surface = []
occur_neko_base = []

# 共起サイズ(window = 1)
for ni in tqdm(neko_index):
    bfr_info_df = neko_mecab_df.loc[ni - 1]
    aft_info_df = neko_mecab_df.loc[ni + 1]

    occur_neko_surface.append(bfr_info_df["surface"])
    occur_neko_surface.append(aft_info_df["surface"])
    occur_neko_base.append(bfr_info_df["base"])
    occur_neko_base.append(aft_info_df["base"])

occur_neko_surface_df = pd.DataFrame(occur_neko_surface, columns=["word"])["word"].value_counts()
occur_neko_base_df = pd.DataFrame(occur_neko_base, columns=["word"])["word"].value_counts()

fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# print(occur_neko_surface_counter)
occur_neko_surface_df.plot(kind="barh", ax=axes[0])
occur_neko_base_df.plot(kind="barh", ax=axes[1])
plt.show()