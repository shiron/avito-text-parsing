# coding=utf-8
from __future__ import unicode_literals
from __future__ import division
from collections import Counter
import string
import re

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import word


COUNT_FREQUENT_WORDS = 5


def tokenize(text):
    """Tokenize original text"""
    tokens = split_text(text)

    # delete punctuation for "-" symbol after split and empty string
    tokens = [token for token in tokens if (token not in string.punctuation and len(token) > 0)]

    # to lower case
    tokens = [token.lower() for token in tokens]

    # tokens is fraud ?
    is_fraud, tokens = detect_fraud(tokens)

    #delete stop words https://github.com/mhq/train_punkt
    stop_words = stopwords.words('russian')
    tokens = [token for token in tokens if (token not in stop_words )]

    #Применить стемминг к токенам
    tokens = stemming(tokens)
    return is_fraud, tokens


def split_text(text):
    """
    Split text
    Считаем, что слово - это последовательность букв, цифр и знаков: _-
    """
    pattern = re.compile(u'[^a-zA-Zа-яА-Я0-9-_]+')
    tokens = pattern.split(text)
    return tokens


def stemming(tokens):
    """Stemming for tokens in text"""
    stemmer = SnowballStemmer("russian")
    tokens = [stemmer.stem(token) for token in tokens]
    return tokens


def detect_fraud(tokens):
    """Detect fraud"""
    new_tokens = []
    is_fraud = False
    for token in tokens:
        is_fraud_word, recovery_token = word.detect_fraud(token)
        if is_fraud_word == True:
            is_fraud = True
        new_tokens.append(recovery_token)
    return is_fraud, new_tokens


def academic_sickness(tokens):
    """Calculate academic sickness for text"""
    if len(tokens) == 0:
        return 0
    else:
        count = Counter(tokens)
        mc = count.most_common(COUNT_FREQUENT_WORDS)

        sum_frequent_words = 0
        for word in mc:
            sum_frequent_words += word[1]
        return sum_frequent_words / len(tokens)