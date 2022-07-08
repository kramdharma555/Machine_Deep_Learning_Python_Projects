# It is used to extract the PDF and Convert into Individual Tokens
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk import word_tokenize
from textblob import TextBlob

import PyPDF2
pdfFile = open('ANABUT.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
print(pdfReader.numPages)

PagE = ''
for i in range(0,4):
    PagE = pdfReader.getPage(i)
    Disp= PagE.extract_text()
    Text_tokens = word_tokenize(Disp)
    print(Disp)
    print(' ')
    print(Text_tokens)
pdfFile.close()
