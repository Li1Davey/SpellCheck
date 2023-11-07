'''
Program by Cristian Pedroza & David Sanchez

code for finding word with max value for two dictionaries
https://stackoverflow.com/questions/68065146/selecting-the-max-value-from-2-dictionaries

'''
from extractData import getDictionaryUnigrams
from extractData import getDictionaryBigrams
from readDocument import getWordUnigrams
from readDocument import getWordBigrams
from docx import Document

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

def getFreqencies(precede, proceed, bigramDict):
    precedeFreq = {}
    proceedFreq = {}
    #*****NEEDS FIXING AS ERROR OCCURS HERE******************
    #Extracts the data that has precede as the first word
    #in the bigram
    precedeDict = bigramDict[bigramDict[:,1] == precede, :]
    #Extracts the data that has proceed as the second word
    #in the bigram
    proceedDict = bigramDict[bigramDict[:,2] == proceed, :]
    #********************************************************
    for pre in precedeDict:
        word = pre[2]
        precedeFreq[word] = pre[0]
    for pro in proceedDict:
        word = pro[1]
        precedeFreq[word] = pro[0]
    return precedeFreq, proceedFreq

def findReplacement(index, unigramParagraph, bigramDict):
    precede = '#EOS#'
    proceed = '#EOS#'
    if (index-1 > -1):
        precede = unigramParagraph[index-1]
    if (index+1 < len(unigramParagraph)):
        proceed = unigramParagraph[index+1]
    precedeFreq, proceedFreq = getFreqencies(precede, proceed, bigramDict)
    #Quick calculation to find word with the maximum frequency that fits between the
    #preceding and proceeding words of the error. This method will be replaced for the finished product
    #since it won't pick word that is similar to the error and has not been tested yet.
    new_word = max(precedeFreq.keys() & proceedFreq.keys(), key=lambda k: (precedeFreq[k], proceedFreq[k]))
    print(new_word)
    return new_word

def fixError(errorList, unigramDoc, bigramDict):
    newList = unigramDoc
    for i in range(len(unigramDoc)):
        for j in range(len(errorList[i])):
            index = errorList[i][j]
            error = unigramDoc[i][index]
            replace = findReplacement(index, unigramDoc[i], bigramDict)
            newList[i][index] = replace
    return newList

###-------main----------

file = 'SmallErrorSample.docx'
unigramDocument = getWordUnigrams(file)
#print("List of Unigrams from Document Results")
#print(unigramDocument)
#print("List of Bigrams from Document Results")
#bigramDocument = getWordBigrams(file)
#print(bigramDocument)

errorList = checkWord(unigramDocument)
#print(errorList)
'''
print("List of Misspelled/Error Word in document Results")
for i in range(len(unigramDocument)):
        for j in range(len(errorList[i])):
            index = errorList[i][j]
            error = unigramDocument[i][index]
            print(error)
'''
bigramDict = getDictionaryBigrams()

fixedDocument = fixError(errorList, unigramDocument, bigramDict)
#Write new document with fixed words once everything is done
output = Document()
for item in fixedDocument:
    output.add_paragraph(item)
output.save('Output.docx')

