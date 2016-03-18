#coding=utf-8
import re

reg_list_fraud = [
    re.compile(u'[а-я0-9-_]+([aeyopxc]+)'), #in the middle and end of word
    re.compile(u'^([aeyopxc]+)[а-я0-9-_]+') #to word that start from fraud
]

def detect_fraud(word):
    """Detect latin symbols in cyrillic text"""
    list_fraud_symbols = []
    for pattern in reg_list_fraud:
        result = pattern.findall(word)
        list_fraud_symbols.extend(result)

    #is_fraud word ? and recovery if is fraud
    if len(list_fraud_symbols) > 0:
        return True, recovery_word(list_fraud_symbols, word)
    else:
        return False, word

def recovery_word(list_fraud_symbols, word):
    """Replace latin symbols to cyrrilic in fraud word"""
    symbols = ('aeopyxc', u'аеорухс')
    tr = {ord(a): ord(b) for a, b in zip(*symbols)}

    for element in list_fraud_symbols:
        word = word.replace(element, element.translate(tr))
    return word



