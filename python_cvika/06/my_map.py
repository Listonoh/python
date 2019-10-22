def my_map(func, arr):
    return [func(j) for j in arr]

print(my_map(lambda x: x +1, [3,9,0,-1,-33333]))