def isPalyndrom(strg):
    len = strg.__len__()
    j = 0
    for i in strg:
        j +=1
        if strg[len - j] != i:
            return False
    return True

def better_palyndrom(wrd):
    return wrd == wrd[::-1]

s = "aaaa haaaa"
print(isPalyndrom(s))
print(better_palyndrom(s))
