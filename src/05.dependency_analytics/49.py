# 40. 係り受け解析結果の読み込み（形態素）Permalink
# # 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．

import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
import os
import re
from tqdm import tqdm
ROOT_PATH = r"C:\Users\shotaro\Desktop\ds\nlp100\src\05.dependency_analytics" # >> 自身の環境に合わせる
os.chdir(ROOT_PATH)
from common import Morph, Chunk


CABOCHA_AI_PATH = "data/ai.ja.txt.parsed"

with open(CABOCHA_AI_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

sents = []
chunk = None
chunks = []
srcs_dict = {}
for line in lines:

    line = line.replace("\n", "")

    if line[0] == "*":
        
        line_info = line.split()
        idx = int(line_info[1])
        dst = int(re.search(r'(.*?)D', line_info[2]).group(1))

        if (dst in srcs_dict) and (dst != -1):
            srcs_dict[dst].append(idx)
        else:
            srcs_dict[dst] = [idx]
        
        if idx != 0:
            chunks.append(chunk)
        else:
            chunks = []

        chunk = Chunk(idx, dst)
    
    elif line == "EOS":
        chunks.append(chunk)
        for k, v in srcs_dict.items():
            chunks[k].update_srsc(v)
        
        sents.append(chunks)
        srcs_dict.clear()

    else:
        morph = Morph(line)
        chunk.update_morph(morph)

for sent in sents:
    nouns = []
    for i, chunk in enumerate(sent):
        if '名詞' in [morph.pos for morph in chunk.morphs]:  # 名詞を含む文節を抽出
            nouns.append(i)
        for i, j in combinations(nouns, 2):  # 名詞を含む文節のペアごとにパスを作成
            path_i = []
            path_j = []
            while i != j:
                if i < j:
                    path_i.append(i)
                    i = sent[i].dst
                else:
                    path_j.append(j)
                    j = sent[j].dst
            if len(path_j) == 0:  # 1つ目のケース
                chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sent[path_i[0]].morphs])
                chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sent[i].morphs])
                chunk_X = re.sub('X+', 'X', chunk_X)
                chunk_Y = re.sub('Y+', 'Y', chunk_Y)
                path_XtoY = [chunk_X] + [''.join(morph.surface for morph in sent[n].morphs) for n in path_i[1:]] + [chunk_Y]
                print(' -> '.join(path_XtoY))
            else:  # 2つ目のケース
                chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sent[path_i[0]].morphs])
                chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sent[path_j[0]].morphs])
                chunk_k = ''.join([morph.surface for morph in sent[i].morphs])
                chunk_X = re.sub('X+', 'X', chunk_X)
                chunk_Y = re.sub('Y+', 'Y', chunk_Y)
                path_X = [chunk_X] + [''.join(morph.surface for morph in sent[n].morphs) for n in path_i[1:]]
                path_Y = [chunk_Y] + [''.join(morph.surface for morph in sent[n].morphs) for n in path_j[1:]]
                print(' | '.join([' -> '.join(path_X), ' -> '.join(path_Y), chunk_k]))