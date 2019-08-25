import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD

documents = os.listdir('text')
documents.sort()
corpus = []
for document in documents:
    with open('text/' + document) as doc:
        corpus.append(doc.read())
vectorizer = CountVectorizer()
count = vectorizer.fit_transform(corpus)
tsvd = TruncatedSVD(3, )
x = count.toarray()
transformed = tsvd.fit_transform(x)
print(transformed)
print(tsvd.components_)
