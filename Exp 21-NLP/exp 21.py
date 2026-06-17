import nltk

sentence = "The smart student reads books"

grammar = "NP: {<DT><JJ><NN>}"

cp = nltk.RegexpParser(grammar)

words = nltk.pos_tag(nltk.word_tokenize(sentence))

tree = cp.parse(words)

print(tree)
