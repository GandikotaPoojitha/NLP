from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "Python is a programming language",
    "Python is used for AI",
    "AI uses machine learning"
]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(docs)

print(tfidf.toarray())
