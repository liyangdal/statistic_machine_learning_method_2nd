import os
import math


word_dict = {}
word_doc_dict = {}
df = 0
documents = os.listdir('text')
for document in documents:
    df += 1
    with open('text/' + document) as doc:
        content = doc.read()
        words = content.split()
        for word in words:
            word_dict.setdefault(word, 1)
            word_doc_dict.setdefault(word, {})
            word_doc_dict[word].setdefault(document, 0)
            word_doc_dict[word][document] += 1

doc_word_counter = {}
df_i_dict = {}
words = word_dict.keys()
for word in words:
    df_i_dict[word] = len(word_doc_dict[word])

tf_j_dict = {}
for word, doc_dict in word_doc_dict.items():
    for doc, count in doc_dict.items():
        tf_j_dict.setdefault(doc, 0)
        tf_j_dict[doc] += count

for document in documents:
    for word in words:
        word_doc_dict[word].setdefault(document, 0)
        tf_ij = word_doc_dict[word][document]
        tf = float(tf_ij)/float(tf_j_dict[document])
        idf = math.log(float(df)/float(df_i_dict[word]))
        tfidf = tf * idf
        print(word + " " + document + ":" + str(tfidf))
