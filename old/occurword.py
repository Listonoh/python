"""
ocurance of words
"""

import sys


#READER = open(sys.argv[1], mode='r')

DIC = {}

Pole = [1,2,3,4,5,6,7,8,8,8,8]
Set = (1,2,3,4,5,6,7,8)

Dict = {x: 0 for x in Set}
for x in Pole:
    Dict[x] += 1

print(Dict)

"""
for line in READER:
    for word in line.split():
        if word in DIC.keys():
            DIC[word] += 1
        else:
            DIC[word] = 1

for i, j in DIC.items():
    print(f"{i} : {j}")
"""
