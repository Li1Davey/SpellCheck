'''
Program by Cristian Pedroza & David Sanchez
'''

def getDictionaryBigrams():
    dict_bigrams = []
    #i = 0
    with open("new_wp_2gram.txt", encoding="utf8") as file:
        for line in file:
            x = line.replace('\n', '')
            a = x.split('\t')
            a[0] = int(a[0])
            dict_bigrams.append(a)
            '''
            #Used to keep track of how many lines are already extracted
            if (i % 10000000 == 0):
                print(i)
            i+=1
            '''
    #print("Bigram Dictionary Results (First 10 lines)")
    #print(dict_bigrams[:10])
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
    #print("Unigram Dictionary Results (First 10 lines)")
    #print(dict(list(dict_unigrams.items())[0: 10]))
    return dict_unigrams
