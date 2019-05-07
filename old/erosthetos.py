from sys import stdin

def funct(do):
    do += 1 
    sito = [True] * do 

    for i in range(2,int(do**0.5) + 2):
        if sito[i]:
            for j in range(i**2, do, i):
                sito[j] = False

    total = 0        
    for i in range(2, do):
        total += sito[i]

    print(total)

do = int(stdin.readline().split()[0])
funct(do)

