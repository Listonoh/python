def my_map(func, arr):
    return [func(arr[j]) for j in range(arr.__len__())]

print(my_map(lambda x: x +1, [3,9,0,-1,-33333]))