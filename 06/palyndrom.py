def isPalyndrom(strg):
    len = strg.__len__()
    j = 0
    for i in strg:
        j +=1
        if strg[len - j] != i:
            return False
    return True

s = "aaaahaaa"
print(isPalyndrom(s))
