import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V
Det -> 'the'
N -> 'cat'
V -> 'runs'
""")

parser = EarleyChartParser(grammar)

sentence = input("Enter sentence: ").split()

result = list(parser.parse(sentence))

if result:
    print("Sentence Accepted")
    for tree in result:
        print(tree)
else:
    print("Sentence Rejected")
