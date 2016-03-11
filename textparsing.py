# -*- coding: utf-8 -*-
import nltk
import string
from nltk.corpus import stopwords

def tokenize(text):
    #apply nltk tokenizer
    tokens = nltk.word_tokenize(text)

    #delete punctiation symbols
    tokens = [i for i in tokens if (i not in string.punctuation)]

    #delete stop words
    stop_words = stopwords.words('russian')
    stop_words.extend(['и', 'в', 'с', 'от', 'o', 'на', 'для', 'по'])
    tokens = [i for i in tokens if (i not in stop_words )]

    return tokens

def write_to_db():
    pass