# 39.Zipfの法則
# # 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
# import pandas as pd
import matplotlib.pyplot as plt
import os
import pandas as pd
from tqdm import tqdm
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\04.morph_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

MECAB_NEKO_PATH = "data/neko.txt.mecab"
neko_mecab_df = pd.read_csv(MECAB_NEKO_PATH)

# 出現頻度算出
word_counts = neko_mecab_df["base"].value_counts().reset_index()
print(word_counts)
# 出現頻度順位算出
word_counts["rank"] = word_counts["base"].rank(ascending=False, method="min")

print(word_counts[["base", "rank"]])

fig, ax = plt.subplots(figsize=(20, 10))
word_counts[["base", "rank"]].plot(x="base", y="rank", ax=ax)
ax.set_xscale("log")
ax.set_yscale("log")

plt.show()

