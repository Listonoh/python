def generateSpacesCNF(n : int):
  # generating all possible tuples
  lis = [(start, start + dif, start +2*dif) for start in range(1,n-1) for dif in range(1,int(n/2)) if start + 2* dif <= n ]
  print(lis)
  out = []
  for s in lis:
    # we don't want when all in tuple are 1 or 0 - not dnf[(1,2,3) or (-1,-2,-3)] => cnf [(1,2,3) and (-1,-2,-3)]
    out.append(f"{s[0]} {s[1]} {s[2]} 0")
    out.append(f"-{s[0]} -{s[1]} -{s[2]} 0")

  with open(f"n{n}.cnf", mode="w") as mFile:
    mFile.write(f"p cnf {n} {len(out)}\n")
    mFile.writelines(line + '\n' for line in out)

if __name__ == "__main__":
  for n in range(6, 12):
    generateSpacesCNF(n)