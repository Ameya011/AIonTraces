#!/usr/bin/python3
import os
import re
from datetime import datetime
import dateutil.parser


def Decimal(d):
    return d

import collections
import collections.abc

filename_pattern = "^(\d*)(-.*)$"

def flatten(d, parent_key='', sep='_'):
    basetime = None
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.abc.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            m= re.match("([0-9]{4}\-[0-9]{2}\-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}Z)", str(v))
            if (m):
                t = m.group(0)
                datetime_object = dateutil.parser.parse(t)
                if (basetime == None):
                    v = ""
                    basetime = datetime_object
                else:
                    diff = datetime_object - basetime
                    v= int(diff.total_seconds())

            items.append((new_key, v))
    return dict(items)


def handleTrace(trace):
    sep = ' '
    d = flatten(trace, sep=sep)
    return re.sub("\n",""," ".join([(a + sep + str(b)) for a, b in zip(d.keys(), d.values())]))

def getTimestamp(filename):
    timestamp = re.search(filename_pattern, filename)
    if (timestamp):
        return int(timestamp.group(1));
    else:
        return 0 

def readFile(name):
    with open(name) as File:
        timestamp = getTimestamp(os.path.basename(name))
        group = timestamp - (timestamp % (5*60))

        D = File.read()
        E = eval(D)
        print(name+"|"+handleTrace(E["system"]["extracted"]) + "|" + str(group))

def readFileData(name):
    with open(name) as File:
        timestamp = getTimestamp(os.path.basename(name))
        group = timestamp - (timestamp % (5*60))

        D = File.read()
        E = eval(D)
    return E


if __name__== "__main__":
    for root, dirs, files in os.walk("../data/15/46", topdown=False):
       for name in files:
          readFile(os.path.join(root, name))


