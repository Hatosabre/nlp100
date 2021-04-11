# 40. 係り受け解析結果の読み込み（形態素）Permalink
# # 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．

import pandas as pd
import matplotlib.pyplot as plt
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
    for m in sent:
        dst = m.dst
        srcs = m.srcs

        verb = None
        for morph in m.morphs:
            if morph.pos == "動詞":
                verb = morph.base
                break
        if verb:
            if dst != -1:
                subs = []
                for src in srcs:
                    dstm = sent[src]
                    for i in range(len(dstm.morphs)):
                        ds = dstm.morphs[-1 - i]
                        if (ds.pos == "助詞") & (ds.surface == "を"):
                            ds_bef = dstm.morphs[-2 - i]
                            if (ds_bef.pos1 == "サ変接続"):
                                subs.append(ds_bef.surface + "を")
                                break
            if len(subs) > 0:
                print(verb + "\t" + " ".join(subs))


                
                

  