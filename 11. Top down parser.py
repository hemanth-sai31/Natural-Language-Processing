import nltk
from nltk import CFG, ChartParser
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'a' | 'the'
    N -> 'man' | 'park' | 'dog' | 'telescope'
    V -> 'saw' | 'walked'
    P -> 'in' | 'with'
""")
parser = ChartParser(grammar)
sentence = "I saw the man in the park".split()
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()  