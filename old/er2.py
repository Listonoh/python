from sys import stdin

x = int(stdin.readline().split()[0])

def eratosthenovo_sito(do):
  do += 1
  sito = [True] * do
 
  for i in range(2, int(do**0.5)+2):
    if sito[i]:
      for j in range(i**2, do, i):
        sito[j]=False
 
  pocet = 0
  for i in range(2, do):
    pocet += sito[i]
  print(pocet)

eratosthenovo_sito(x)