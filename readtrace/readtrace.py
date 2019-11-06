#!/usr/bin/python3

def Decimal(d):
    return d

with open("1436857390-cc20147a-fa86-4c59-bff4-5d13fc63ae5b:0-2-0-f-f-2f-4-6-0-3-0") as File:
    D= File.read(100000)
    E= eval(D)
    print(E["system"]["extracted"])
