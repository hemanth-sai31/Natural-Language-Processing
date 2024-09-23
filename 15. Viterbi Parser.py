import nltk
from nltk import PCFG, ViterbiParser
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | V [0.3]
    NP -> Det N [0.6] | N [0.4]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'cat' [0.5] | 'dog' [0.5]
    V -> 'chased' [0.9] | 'saw' [0.1]
""")
def parse_sentence_pcfg(sentence):
    tokens = sentence.split()
    parser = ViterbiParser(grammar)
    try:
        trees = list(parser.parse(tokens))
        return trees[0] 
    except IndexError:
        return None
sentences = [
    "the cat chased the dog",
    "a dog saw the cat"
]
for sentence in sentences:
    parse_tree = parse_sentence_pcfg(sentence)
    if parse_tree:
        print(f"Parse tree for '{sentence}':")
        print(parse_tree)
        parse_tree.pretty_print()
    else:
        print(f"No parse tree found for sentence: '{sentence}'")