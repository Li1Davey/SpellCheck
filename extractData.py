'''
David Sanchez
'''

def getDictionaryBigrams():
    file = 'wp_2gram.txt'
    fp = open(file, encoding="utf8")
    total = 0
    dict_bigrams = []
    for line in fp.readlines():
        x = line.replace('\n', '')
        a = x.split('\t')
        total += int(a[0])
        a[0] = int(a[0])
        #print(a)
        dict_bigrams.append
    print(total)
    return dict_bigrams, total
