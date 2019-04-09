"""
posfix calculator
"""

import sys


def calculate(mylist):
    """
    posfix calculator
    """
    stack = []
    for i in mylist:
        if i.isnumeric():
            stack.append(i)
            print(f"apending {i}")
        else:
            stack.append(str(eval(stack.pop()+ i + stack.pop())))
    return stack.pop()

A = calculate(sys.argv[1:])
print(A)
