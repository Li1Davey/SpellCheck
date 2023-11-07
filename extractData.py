'''
David Sanchez
'''

def getDictionaryBigrams():
    dict_bigrams = []
    i = 0
    with open("new_wp_2gram.txt", encoding="utf8") as file:
        for line in file:
            x = line.replace('\n', '')
            a = x.split('\t')
            a[0] = int(a[0])
            if(len(a)==3):
                dict_bigrams.append(a)
            '''
            if (i % 10000000 == 0):
                print(i)
            i+=1
            '''
    #print("Finished")
    return dict_bigrams

def getDictionaryUnigrams():
    file = 'wp_1gram.txt'
    fp = open(file, encoding="utf8")
    dict_unigrams = {}
    for line in fp.readlines():
        x = line.replace('\n', '') 
        a = x.split('\t')
        count = int(a[0])
        word = a[1]
        dict_unigrams[word] = count/1548800152
    return dict_unigrams
