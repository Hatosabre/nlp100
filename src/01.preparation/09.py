STR = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

import random
def change_sample(sents):
    sent_list = sents.split()
    change_sent_list = []
    for sent in sent_list:
        if len(sent) <= 4:
            change_sent_list.append(sent)

        else:
            top = sent[0]
            middle = sent[1:-1]
            bottom = sent[-1]

            change_middle = "".join(random.sample(middle, len(middle)))
            change_sent_list.append(top + change_middle + bottom)
    
    return " ".join(change_sent_list)

print(change_sample(STR))