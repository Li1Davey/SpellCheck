'''
Cristian Pedroza

'''
from extractData import getDictionaryUnigrams
from readDocument import getWordUnigrams
from docx import Document

def checkWord():

    input = Document('SmallErrorSample.docx')
    paragraphs = []

    for para in input.paragraphs:
        p = para.text
        paragraphs.append(p)

    unigramDict, total = getDictionaryUnigrams()
    documentUnigrams = getWordUnigrams(paragraphs)
    errorList = []
    print(documentUnigrams)

    for innerlist in documentUnigrams:
        for i in range(len(innerlist)):
            word = innerlist[i]
            if(unigramDict.get(word) == None):
                errorList.append(i)

    print(errorList)

###-------main----------

print(checkWord())

