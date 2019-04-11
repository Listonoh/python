def mrange(*args):
    beg, step = 0, 1
    if args.__len__() == 1:
        limit = args[0]
    if args.__len__() >= 2:
        limit = args[1]
        beg = args[0]
    if args.__len__() == 3:
        step = args[2]
    if args.__len__() > 3:
        raise Exception("argument error")
    while beg < limit:
        yield beg
        beg =+ step
