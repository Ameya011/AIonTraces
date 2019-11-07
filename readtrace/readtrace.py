#!/usr/bin/python3
import os
import re

def Decimal(d):
    return d


import collections
import collections.abc

filename_pattern = "^(\d*)(-.*)$"

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.abc.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def handleTrace(trace):
    sep = ' '
    d = flatten(trace, sep=sep)
    return re.sub("\n",""," ".join([(a + sep + str(b)) for a, b in zip(d.keys(), d.values())]))

def getTimestamp(filename):
    timestamp = re.search(filename_pattern, filename)
    if (timestamp):
        return timestamp.group(1);
    else:
        return ""

def readFile(name):
    with open(name) as File:
        timestamp = getTimestamp(os.path.basename(name))
        D = File.read()
        E = eval(D)
        print(name+"|"+handleTrace(E["system"]["extracted"]) + "|" + timestamp)

for root, dirs, files in os.walk("../data/15/46", topdown=False):
   for name in files:
      readFile(os.path.join(root, name))


