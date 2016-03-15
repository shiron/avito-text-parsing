#coding=utf-8
from __future__ import unicode_literals
from astropy.utils.compat.futures import ThreadPoolExecutor
from textparsing import tokenize
import os
from collections import Counter


DATA_DIR = './test/'
COUNT_WORKERS = 1

def parse(file):
    #open text file and get tokens
    with open(DATA_DIR + file) as text_file:
        is_fraud, tokens = tokenize(text_file.read())

    #calculate count of tokens
    count = Counter(tokens)
    mc = count.most_common(5)
    for key,value in mc:
        print key, value
    #write to db


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=COUNT_WORKERS) as executor:
        file_list = os.listdir(DATA_DIR)
        for file in file_list:
            executor.submit(parse, file)
