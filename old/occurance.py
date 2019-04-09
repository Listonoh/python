"""
something smart
"""

import sys

WORD = sys.argv[1]

for i in set(WORD):
    print(f"{i} {WORD.count(i)}")

"""
DIC = {}
for i in WORD:
    if i in DIC.keys():
        DIC[i] += 1
    else:
        DIC[i] = 1

for i, j in DIC.items():
    print(f"{i} : {j}")
"""
