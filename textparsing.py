#coding=utf-8
from __future__ import unicode_literals
import string
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def tokenize(text):
    tokens = clear_and_split_text(text)

    #delete punctuation symbols
    tokens = [token for token in tokens if (token not in string.punctuation)]

    #to lower case
    tokens = [token.decode('utf-8').lower() for token in tokens]

    #delete stop words https://github.com/mhq/train_punkt
    stop_words = stopwords.words('russian')
    tokens = [token for token in tokens if (token not in stop_words )]

    #Применить стемминг к токенам
    tokens = stemming(tokens)

    #Вычислить мошенничество и привести слова в нормальную форму
    is_fraud, tokens = detect_fraud(tokens)

    return is_fraud, tokens

def clear_and_split_text(text):
    #TODO очистить текст от спецсимволов
    #get tokens from text
    #tokens = nltk.word_tokenize(text, language='russian')
    #tokens = nltk.wordpunct_tokenize(text)
    tokens = text.split()
    return tokens

def stemming(tokens):
    new_tokens = []
    stemmer = SnowballStemmer("russian")
    for token in tokens:
        word = stemmer.stem(token)
        print word
        new_tokens.append(word)
    return new_tokens

def detect_fraud(tokens):
    """примеры слов:
    read - true
    пaчка - false
    пачкa - false
    anti-мир - true
    ВЛКСМ - true
    FSB - true
    oкнo - false
    kатя - false
    катя - true
    """
    new_tokens = []
    for token in tokens:
        new_tokens.append(token)

    return False, new_tokens

def write_to_db():
    pass