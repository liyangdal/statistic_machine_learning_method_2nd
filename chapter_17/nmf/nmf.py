import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import NMF

documents = os.listdir('text')
documents.sort
corpus = []
for document in documents:
    with open('text/' + document) as doc:
        corpus.append(doc.read())
vectorizer = CountVectorizer()
count = vectorizer.fit_transform(corpus)
nmf = NMF(n_components=3, random_state=1, alpha=.1, l1_ratio=.5)
transformed = nmf.fit_transform(count)
print(transformed)
print(nmf.components_)
