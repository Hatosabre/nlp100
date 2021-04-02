TEST_WORDS = "I am an NLPer"
TEST_WORDS_LIST = TEST_WORDS.split()

# if in word ⇒ 'I ',  a', 'am', 'm ' ・・・
# if in list ⇒ ['I', 'am'], ['am', 'an'] ・・・
def n_gram(word_or_list, n):
    size = len(word_or_list)
    roop_count = size - n + 1

    n_gram_list = []
    for i in range(roop_count):
        n_gram_list.append(word_or_list[i: i+n])
    
    return n_gram_list

print("WORD BI GRAM", n_gram(TEST_WORDS_LIST, 2))
print("LETTER BI GRAM", n_gram(TEST_WORDS, 2))
