#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:51:57 2018

@author: xingyuxuan
"""

import pyLDAvis.gensim
from gensim import corpora
from gensim.models import LdaModel

def get_corpus_dictionary():
    documents = open("yelp.txt")
    stoplist = set('for a of the and to in'.split())
    texts = [[word for word in document.lower().split() if word not in stoplist]
             for document in documents]

    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] <800]
             for text in texts]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    return corpus, dictionary

def test_lda():
    corpus, dictionary = get_corpus_dictionary()
    lda = LdaModel(corpus=corpus,num_topics=20)
    data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    pyLDAvis.show(data,open_browser=True)

if __name__ == "__main__":
    test_lda()

