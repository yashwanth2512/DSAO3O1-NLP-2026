sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    tag = "NOUN"

    if word.endswith("ing"):
        tag = "VERB"
    elif word.lower() in ["is", "am", "are"]:
        tag = "VERB"
    elif word[0].isupper():
        tag = "PROPER NOUN"

    print(word, "->", tag)
