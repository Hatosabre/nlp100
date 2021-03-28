# 40. 係り受け解析結果の読み込み（形態素）Permalink
# # 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．

import pandas as pd
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\05.dependency_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)
from common import Morph


CABOCHA_AI_PATH = "data/ai.ja.txt.parsed"

with open(CABOCHA_AI_PATH, "r") as f:
    lines = f.readlines()

sents = []
morphs = []
for line in lines:
    line = line.replace("\n", "")

    if line[0] == "*":
        pass

    else:
        morph = Morph(line)
        morphs.append(morph)

print(morphs)