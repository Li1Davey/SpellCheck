'''
code from
https://stackoverflow.com/questions/48869423/how-do-i-copy-the-contents-of-a-word-document
'''
from docx import Document

#_Main---------------------------------------------------
input = Document('Source.docx')
paragraphs = []
for para in input.paragraphs:
    p = para.text
    paragraphs.append(p)

#print(paragraphs)
output = Document()
for item in paragraphs:
    output.add_paragraph(item)
output.save('New.docx')
