
def Goldberg(V, E, z, s, c):  # vertexes edges zdroj stok capacity
    f = {(i, j): 0 for i in V for j in V}
    h = [0 for v in V]
    h[z] = len(V) 

    for e in E:
        if z in e:
            v = e[0]
            if e[0] == z:
                v = e[1]
            f[(z, v)] = c[e]

    finish = False
    while not finish:
        finish = True
        for u in V:
            if u in (z, s): continue
            dif = 0

            for v in V:
                if u != v:
                    dif += f[(v, u)] - f[(u, v)]

            if dif > 0:
                finish, find = False, False
                for e in E:
                    if u in e:
                        if u == e[0]:
                            v = e[1]
                            delta = c[e] - f[e]
                            minim = min([dif, delta])
                            if h[u] > h[v] and minim > 0:
                                find = True
                                f[e] += minim
                                dif -= minim
                        else:
                            v = e[0]
                            delta = f[e]
                            minim = min([dif, delta])
                            if h[u] > h[v] and minim > 0:
                                find = True
                                f[e] -= minim
                                dif -= minim
                if not find and u != s:
                    h[u] += 1
    return {key: item for key, item in f.items() if item != 0}


#testing data from "pruvodce svetem algoritmu, from Martin Mares"
V = range(6)
e = [(0, 1), (0, 3), (1, 2), (1, 4), (3, 2), (3, 4), (4, 5), (2, 5)]
z = 0
s = 5
c = {e[0]: 10, e[1]: 10, e[2]: 7, e[3]: 5,
     e[4]: 9, e[5]: 3, e[6]: 10, e[7]: 10}

print(Goldberg(V, e, z, s, c))
