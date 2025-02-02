#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

plt.xlabel(args.key)
plt.ylabel("Count")

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10][::-1]
for k,v in items:
    print(k,':',v)
    plt.bar(k, v)

plt.savefig(args.key + '.png')    
