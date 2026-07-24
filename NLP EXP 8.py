sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    if word.lower() in ["is", "am", "are", "was", "were"]:
        tag = "VERB"
    elif word.endswith("ing"):
        tag = "VERB"
    elif word[0].isupper():
        tag = "PROPER NOUN"
    else:
        tag = "NOUN"

    print(word, "->", tag)
