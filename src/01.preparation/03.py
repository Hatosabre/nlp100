STR = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
rep_str = STR.replace(",", "")
def len_str(x): return str(len(x))
word_list = "".join(map(len_str, rep_str.split()))
print(word_list)