# coding=utf-8
from __future__ import unicode_literals
from astropy.utils.compat.futures import ThreadPoolExecutor
from db_manager import write_to_db, create_db
import document
import os
import argparse


DATA_DIR = './text_files/'
COUNT_WORKERS = 1
PATH_DB = 'result.db'


def parse(file, db_path):
    # open text file and get tokens
    print('In processing: {}'.format(file))
    with open(DATA_DIR + file) as text_file:
        is_fraud, tokens = document.tokenize(text_file.read().decode('utf-8'))

    # get academic sickness
    ac = document.academic_sickness(tokens)

    # write to db
    write_to_db(db_path, file, is_fraud, ac)


def run_pools(files_dir, count_workers, db_path):
    """Run parse files in threads"""
    with ThreadPoolExecutor(max_workers=count_workers) as executor:
        file_list = os.listdir(files_dir)
        for file in file_list:
            executor.submit(parse, file, db_path)

if __name__ == "__main__":
    m = argparse.ArgumentParser(description="Run parsing text")
    m.add_argument("--files_dir", "-f", type=str, default="./text_files", help="Path to dir with text files")
    m.add_argument("--count_workers", "-c", type=int, default=1, help="Count of workers in thread pool")
    m.add_argument("--db_path", "-d", type=str, default="result.db", help="Path to create db")
    options = vars(m.parse_args())

    # create db
    create_db(options['db_path'])

    #run workers
    run_pools(options['files_dir'], options['count_workers'], options['db_path'])

