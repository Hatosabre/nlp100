class Morph:
    def __init__(self, info):
        surface, pos, pos1, base = self.split(info)
        self.surface = surface
        self.pos = pos
        self.pos1 = pos1
        self.base = base

    def split(self, info):
        word_infos = info.split("\t")
        surface = word_infos[0]
        sub_info = word_infos[1].split(",")
        pos = sub_info[0]
        pos1 = sub_info[1]
        base = sub_info[6]
        return (surface, pos, pos1, base)
    def __str__(self):
        return self.surface + "," + self.pos + "," + self.pos1 +  "," + self.base

# * 1 14D 2/3 -1.212364
class Chunk:
    def __init__(self, idx, dst):
        self.idx = idx
        self.morphs = []
        self.dst = dst
        self.srcs = []
    
    def update_morph(self, morph):
        self.morphs.append(morph)
    
    def update_srsc(self, srcs):
        self.srcs = srcs
        