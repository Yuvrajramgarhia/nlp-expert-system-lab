import nltk 
from nltk.tokenize import word_tokenize 

nltk.download('punkt')

sentence = "Tokenizing a sentence is the first step in text analysis"

words = word_tokenize(sentence)

print("Tokenized Words:", words)