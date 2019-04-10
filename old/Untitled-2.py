import itertools

instring = ""

for i in range(32):
    instring += "1"

for i in range(32):
    instring += "0"

for i in ["".join(x) for i in range(1,9) for x in itertools.permutations(instring, 64) ]:
    print(i)
