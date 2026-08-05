import nltk
from nltk.tokenize import word_tokenize

# Download required resources (only first time)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")

tokens = word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

print("\nPOS Tagged Words:")
for word, tag in tagged:
    print(word, "->", tag)
