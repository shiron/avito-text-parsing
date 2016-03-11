# -*- coding: utf-8 -*-
from astropy.utils.compat.futures import ThreadPoolExecutor
from textparsing import tokenize
import os
from collections import Counter


DATA_DIR = './text_files/'
COUNT_WORKERS = 4

def parse(file):
    tokens = tokenize(open(DATA_DIR + file).read())
    tokens_new = []
    for token in tokens:
        tokens_new.append(token.decode('utf-8'))

    count = Counter(tokens_new)
    print(count.most_common(5))


with ThreadPoolExecutor(max_workers=COUNT_WORKERS) as executor:
    #get file list
    file_list = os.listdir(DATA_DIR)
    for file in file_list:
        executor.submit(parse, file)
