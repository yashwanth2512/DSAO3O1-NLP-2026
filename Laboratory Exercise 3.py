import nltk
import spacy
from nltk.tokenize import word_tokenize

# Download NLTK resources (only first time)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

sentence = input("Enter a sentence: ")

# NLTK POS Tagging
tokens = word_tokenize(sentence)
nltk_tags = nltk.pos_tag(tokens)

print("\nNLTK POS Tags:")
for word, tag in nltk_tags:
    print(word, "->", tag)

# spaCy POS Tagging
doc = nlp(sentence)

print("\nspaCy POS Tags:")
for token in doc:
    print(token.text, "->", token.pos_)
