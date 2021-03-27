# curl https://nlp100.github.io/data/neko.txt > $ROOT_PATH/data/neko.txt

def load_neko(neko_path):
    with open(neko_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    lines_drop_n_and_space = []

    # 改行と空白のみ除去
    for line in lines:
        line = line.replace('\n', '')
        line = line.replace('\u3000', '')
        lines_drop_n_and_space.append(line)
    return lines_drop_n_and_space