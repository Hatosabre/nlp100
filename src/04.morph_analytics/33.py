# 33. 「AのB」Permalink
# # 2つの名詞が「の」で連結されている名詞句を抽出せよ．

import pandas as pd
import os
from tqdm import tqdm
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\04.morph_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)

MECAB_NEKO_PATH = "data/neko.txt.mecab"
neko_mecab_df = pd.read_csv(MECAB_NEKO_PATH)

# 愚策(助詞連体型の”の”の直前・直後が名詞であるものを取得)
middile_no_index = neko_mecab_df.query(
    'base == "の" and pos == "助詞" and pos1 == "連体化"'
).index.tolist()

noun_phrase_list = []
for m_index in middile_no_index:
    around_word_infos = neko_mecab_df.loc[[m_index - 1, m_index + 1]].values
    
    if around_word_infos[0][1] == "名詞" and around_word_infos[1][1] == "名詞":
        noun_phrase_list.append(around_word_infos[0][0] + "の" + around_word_infos[1][0])

print(noun_phrase_list)