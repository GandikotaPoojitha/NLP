import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'Ram'
VP -> V NP
V -> 'likes'
NP -> 'mango'
""")

parser = nltk.EarleyChartParser(grammar)

sentence = "Ram likes mango".split()

for tree in parser.parse(sentence):
    print(tree)
