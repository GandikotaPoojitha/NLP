import spacy

nlp = spacy.load("en_core_web_sm")

text = "Virat Kohli plays for India."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)
