"""
kecy je to selection sort
"""

x = [2, 4, 4, 2, 0, 9, 8]

z = [a for a in x if a ]

for i in range(x.__len__()):
    for j in range(i, x.__len__()):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]

print(x)
