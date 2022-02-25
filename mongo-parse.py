#!/usr/bin/env python3

import argparse
import sys

if len(sys.argv) != 3:
    print("Usage: ./mongo-parse.py -p <path_to_mongo-hashdump_file>")
    sys.exit(0)

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="Path to mongo hash dump file")
args = parser.parse_args()

fp = args.path

mongo_dump = open(fp, 'r')

for x in range(0, 20):
    mongo_read = mongo_dump.readline()
    if 'rocket.cat' in mongo_read:
        continue
    username = mongo_read.split(', "name"')[1].split('"')[1]
    hashlist = mongo_read.split(': {')[2].split('"')[3]
    print(username + ":" + hashlist)

mongo_dump.close()
