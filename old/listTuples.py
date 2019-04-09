"""
create list of tuples
"""

X = [(a, b, a*b) for a in range(1,11) for b in range(1,11) if b % 2 == 0 ]
print(X)
