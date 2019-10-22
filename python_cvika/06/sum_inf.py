def sum(*args):
    temp = 0
    for i in args:
        temp += int(i)
    return temp

print(sum(1,2,3,4,5,-1))