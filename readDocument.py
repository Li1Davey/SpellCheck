'''
code for reading and creating a copy of a document from
https://stackoverflow.com/questions/48869423/how-do-i-copy-the-contents-of-a-word-document

code for getting word bigrams from text from
https://stackoverflow.com/questions/21844546/forming-bigrams-of-words-in-list-of-sentences-with-python
'''
from docx import Document
from nltk import word_tokenize 
from nltk.util import ngrams

#_Main---------------------------------------------------
input = Document('SmallErrorSample.docx')
paragraphs = []
bigrams = []
for para in input.paragraphs:
    p = para.text
    paragraphs.append(p)

for para in paragraphs:
    token = word_tokenize(para)
    b = list(ngrams(token, 2))
    bigrams.append(b)

bigrams.remove([])
#print(bigrams)

output = Document()
for item in paragraphs:
    output.add_paragraph(item)
output.save('Output.docx')
