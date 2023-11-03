'''
David Sanchez
'''

def getDictionaryBigrams():
    file = 'wp_2gram.txt'
    fp = open(file, encoding="utf8")
    limit = 10
    total = 0
    dict_bigrams = []
    for line in fp.readlines():
        if(limit > 0):
            x = line.replace('\n', '')
            a = x.split('\t')
            total += int(a[0])
            a[0] = int(a[0])
            #print(a)
            dict_bigrams.append
        limit-=1
    print(total)
    return dict_bigrams, total
