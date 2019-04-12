def mrange(*args):
    beg, step, limit = 0, 1, 0
    if args.__len__() == 1:
        limit = args[0]
    if args.__len__() >= 2:
        limit = args[1]
        beg = args[0]
    if args.__len__() == 3:
        step = args[2]
    if args.__len__() > 3 | args.__len__() < 1:
        raise Exception("argument error")
    if step > 0:
        while beg < limit:
            yield beg
            beg += step
    else:
        while beg > limit:
            yield beg
            beg += step


# testing data
lis = list(i for i in mrange(10))
print(lis)

lis = list(i for i in mrange(1, 10))
print(lis)

lis = list(i for i in mrange(10, 1, -1))
print(lis)

lis = list(i for i in range(10, 1, -1))
print(lis)
