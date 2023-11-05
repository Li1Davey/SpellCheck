'''
Cristian Pedroza

'''
from extractData import getDictionaryUnigrams
from readDocument import getWordUnigrams
from docx import Document

def checkWord():

    file = 'SmallErrorSample.docx'
    unigramDict, total = getDictionaryUnigrams()
    documentUnigrams = getWordUnigrams(file)
    errorList = []
    # print(documentUnigrams)

    for innerlist in documentUnigrams:
        for i in range(len(innerlist)):
            word = innerlist[i]
            if(unigramDict.get(word) == None):
                errorList.append(i)
                
    print(errorList)

###-------main----------

print(checkWord())

