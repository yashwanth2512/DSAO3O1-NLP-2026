from collections import Counter

# Input sentence
sentence = input("Enter a sentence: ").lower().split()

# Count words
word_count = Counter(sentence)

# Vocabulary size
V = len(word_count)

# Total words
N = len(sentence)

# Word to calculate probability
word = input("Enter the word: ").lower()

# Laplace Smoothing Formula
probability = (word_count[word] + 1) / (N + V)

print("\nWord Count:", word_count[word])
print("Total Words:", N)
print("Vocabulary Size:", V)
print("Laplace Smoothed Probability =", round(probability, 4))
