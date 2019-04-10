"""
generator of database
"""

with open("data.txt", 'w') as DAT:
    for i in range(100000):
        DAT.write(f"insert Osoba value({i}, '{i*102846732937% 1000000}', {i*39473623433% 1000000}, '{1900+(i*3463287462834%120)}-{(i^21)%12+1}-{(i^21)%12+1}', NULL);\n")
    