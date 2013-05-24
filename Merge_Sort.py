#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time

def mergesort(seq):
    if len(seq) <= 1:
        return seq
    else:
        leftList = seq[:len(seq)/2]
        rightList = seq[len(seq)/2:]
        return merge(mergesort(leftList), mergesort(rightList))

def merge(leftList, rightList):
    newList = []
    while leftList != [] and rightList != []:
        if leftList[0] <= rightList[0]:
            newList.append(leftList[0])
            del leftList[0]
        else:
            newList.append(rightList[0])
            del rightList[0]

    while leftList != []:
        newList.append(leftList[0])
        del leftList[0]

    while rightList != []:
        newList.append(rightList[0])
        del rightList[0]

    return newList
"""
list = []
for rand in range(10000):
    rand = random.randint(1,10000)
    list.append(rand)

ausgabe = mergesort(list)
print ausgabe
"""
