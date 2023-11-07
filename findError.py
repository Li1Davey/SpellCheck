'''
Cristian Pedroza & David Sanchez

code for finding word with max value for frequency for preceding and proceeding words
https://stackoverflow.com/questions/68065146/selecting-the-max-value-from-2-dictionaries

'''
from extractData import getDictionaryUnigrams
from extractData import getDictionaryBigrams
from readDocument import getWordUnigrams
from readDocument import getWordBigrams
from docx import Document
import pickle

def checkWord(documentUnigrams):
    unigramDict = getDictionaryUnigrams()
    errorList = []
    for innerlist in documentUnigrams:
        paragraphErrors = []
        for i in range(len(innerlist)):
            word = innerlist[i]
            if(unigramDict.get(word) == None):
                paragraphErrors.append(i)
        errorList.append(paragraphErrors)   
    return errorList

def getFreq(precede, proceed, bigramDict):
    precedeFreq = {}
    proceedFreq = {}
    #Extracts the data that has precede as the first word
    #in the bigram
    #NEED FIXING AS ERROR OCCURS HERE
    precedeDict = bigramDict[bigramDict[:,1] == precede, :]
    #Extracts the data that has proceed as the second word
    #in the bigram
    proceedDict = bigramDict[bigramDict[:,2] == proceed, :]
    for pre in precedeDict:
        word = pre[2]
        precedeFreq[word] = pre[0]
    for pro in proceedDict:
        word = pro[1]
        precedeFreq[word] = pro[0]
    return precedeFreq, proceedFreq

def findReplacement(error, index, unigramParagraph, bigramDict):
    precede = '#EOS#'
    proceed = '#EOS#'
    if (index-1 > -1):
        precede = unigramParagraph[index-1]
    if (index+1 < len(unigramParagraph)):
        proceed = unigramParagraph[index+1]
    
    precedeFreq, proceedFreq = getFreq(precede, proceed, bigramDict)
    #Quick calculation to find word with the maximum frequency that fits between the
    #preceding and proceeding words of the error. This method will be replaced for the finished product
    new_word = max(precedeFreq.keys() & proceedFreq.keys(), key=lambda k: (precedeFreq[k], proceedFreq[k]))
    print(new_word)
    return new_word

def fixError(e, u, d):
    newList = u
    for i in range(len(u)):
        for j in range(len(e[i])):
            index = e[i][j]
            error = u[i][index]
            #print(error)
            replace = findReplacement(error, index, u[i], d)
            newList[i][index] = replace
    return newList

###-------main----------

file = 'SmallErrorSample.docx'
documentUnigrams = getWordUnigrams(file)
#documentBigrams = getWordBigrams(file)

errorlist = checkWord(documentUnigrams)
print(errorlist)

bigramDict = getDictionaryBigrams()

documentFixed = fixError(errorlist, documentUnigrams, bigramDict)
output = Document()
for item in documentFixed:
    output.add_paragraph(item)
output.save('Output.docx')

