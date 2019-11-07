#!/usr/bin/python3

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


with open("1436857390-cc20147a-fa86-4c59-bff4-5d13fc63ae5b:0-2-0-f-f-2f-4-6-0-3-0") as File:
    D = File.read()
    E = eval(D)
    print(E["system"]["extracted"])
    print(handleTrace(E["system"]["extracted"]))
