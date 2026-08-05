import nltk
from nltk.tokenize import word_tokenize

# Download required NLTK resources (only first time)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Input sentence
text = input("Enter a sentence: ")

# Tokenization
tokens = word_tokenize(text)

# POS Tagging
pos_tags = nltk.pos_tag(tokens)

print("\nTokens:")
print(tokens)

print("\nPOS Tags:")
for word, tag in pos_tags:
    print(word, ":", tag)
