import itertools
import json

def load_function(input_file):
    comands = {}
    with open(input_file, mode='r') as inp:
        for line in inp:
            l = line.split()
            comands[l[0]] = (l[1], l[2])
    return comands

def is_in_alphabet(ch):
    return ch == '0' or ch == '1'

def is_accepting_state(ch):
    return ch == '1'

def iterate(input_file, comands):
    state = '0'
    with open(input_file) as inp:
        for line in inp:
            for char in line:
                if is_in_alphabet(char):
                    state = comands[state][int(char)]
                
    return state

def iterateText(text, comands):
    state = '0'
    for char in text:
        #print(f"{state} , {char} : {is_in_alphabet(char)}")
        if is_in_alphabet(char):
            state = comands[state][int(char)]
        
    return state


COMANDS = load_function("text.in")
print(COMANDS)
#STATE = iterate("input.in", COMANDS)
#print(iterateText("011010", COMANDS))


correct_states= []

words = ["".join(x) for i in range(1,9) for x in itertools.product("01", repeat=i) ]

for item in words:
    STATE = iterateText(item, COMANDS)
    if is_accepting_state(STATE):
        correct_states.append(item)


print(correct_states.__len__())
print(words.__len__())

print(correct_states)


