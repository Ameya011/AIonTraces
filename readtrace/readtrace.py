#!/usr/bin/python3
import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

def Decimal(d):
    return d


import collections
import collections.abc


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
    return " ".join([(a + sep + str(b)) for a, b in zip(d.keys(), d.values())])


with open(r"C:\Users\Ranieri\PycharmProjects\AIonTraces\data\export\14\43\06\75\00\1443067799-cc20147a-fa86-4c59-bff4-5d13fc63ae5b_0-2-0-d-800000c") as File:
    D = File.read()
    E = eval(D)
    print(E["system"]["extracted"])
    print(handleTrace(E["system"]["extracted"]))
