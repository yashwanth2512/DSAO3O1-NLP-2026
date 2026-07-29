from collections import Counter

# Input sentence
sentence = input("Enter a sentence: ").lower().split()

# Create bigrams
bigrams = []
for i in range(len(sentence) - 1):
    bigrams.append((sentence[i], sentence[i + 1]))

# Count bigrams and words
bigram_count = Counter(bigrams)
word_count = Counter(sentence)

# Input words
first = input("Enter first word: ").lower()
second = input("Enter second word: ").lower()

# Check if bigram exists
if bigram_count[(first, second)] > 0:
    probability = bigram_count[(first, second)] / word_count[first]
    print("\nBigram Found")
else:
    probability = word_count[second] / len(sentence)
    print("\nBigram Not Found")
    print("Using Backoff (Unigram Probability)")

print("Probability =", round(probability, 4))
