#We have to import the TextBlob Module for this spelling correction
from textblob import TextBlob
#words user defined variable/obeject is used to hold the sentences
words = ["Cmptr", "Scnce", "Lngueg"]
#Correctword holds the dummy arrays to store many values 
CorrectWord = []
#For loop is performed here to get the number of characters/words will be appended 
for i in words:
    CorrectWord.append(TextBlob(i))
#For testing the mistaken words
print("Mistaken Word", words)
#To get the corrected words and one more loop is being used to show each corrected word
print("Corrected Word is")
for i in CorrectWord:
    print(i.correct()), end="")
