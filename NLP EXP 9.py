import re

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    if re.search("ing$", word):
        tag = "VERB"
    elif re.search("ly$", word):
        tag = "ADVERB"
    elif re.search("ed$", word):
        tag = "VERB"
    elif re.search("ion$", word):
        tag = "NOUN"
    else:
        tag = "NOUN"

    print(word, "->", tag)
