"""
spliter
"""

import sys

with open(sys.argv[1], mode='r') as READER:
    for line in READER:
        for word in line.split():
            print(word)
