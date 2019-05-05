"""
posfix calculator
"""

import sys


def calculate(line):
    try:
        arr_line = line.split()
        stack = []
        for value in arr_line:
            if value in "+-*/":
                frs, scn = stack.pop(), stack.pop()
                strk = f"{scn} {value} {frs}"
                stack.append(int(eval(strk)))
            else:
                stack.append(value)
        return int(stack.pop()) if len(stack) == 1 else "Malformed expression"
    except ZeroDivisionError:
        return "Zero division"
    except:
        return "Malformed expression"


if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip() != "":
            print(calculate(line))
