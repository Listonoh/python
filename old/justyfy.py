"""
justyfy to left
"""

import sys


MAXL = int(sys.argv[1])
BUF = []
BLEN = 0


def printb():
    """
    prints and delete BUF
    """
    global BLEN
    for wor in BUF:
        print(wor, end=' ')
    print()
    BUF.clear()
    BLEN = 0
    return 0

def buffer_add(mword):
    """
    recive word if buffer_add is full it prints
    """
    if BLEN + mword.__len__() > MAXL:
        printb()

    BUF.append(mword)
    return BLEN + mword.__len__() + 1

with open(sys.argv[2]) as FIL:
    for line in FIL:
        for word in line.split():
            BLEN = buffer_add(word)

if BUF.__len__() > 0:
    printb()

