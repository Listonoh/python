def fib_n(n): # only for n > 1
    arr = [0,1]
    for i in range(n - 2):
        arr.append(arr[i] + arr[i+1])
    return arr


def fib_gen(n):
    a, b, i = 0, 1, 0
    while i < n:
        yield a
        a, b = b, a+b
        i += 1


print(fib_n(7)) 
for i in fib_gen(7):
    print(i)