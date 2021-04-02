def n_gram(word_or_list, n):
    size = len(word_or_list)
    roop_count = size - n + 1

    n_gram_list = []
    for i in range(roop_count):
        n_gram_list.append(word_or_list[i: i+n])
    
    return n_gram_list