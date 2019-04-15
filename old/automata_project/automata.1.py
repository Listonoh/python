import itertools
import json

class automaton:
    # state - list of tuples (state, position)
    def __init__(self, file):
        with open(file, mode='r') as inp:
            self.mess = json.load(inp)
        self.state = [(self.mess["s0"][0], self.mess["s0"][1])]


    def is_in_alphabet(self, ch):
        for i in self.mess["alfabet"]:
            if i == ch:
                return True
        return False


    def is_accepting_state(self, state):
        for i in self.mess["sA"]:
            if i == state:
                return True
        return False


    def move(self, mtuple, text, stat):
        for instruction in mtuple[stat[0]]:
            if instruction[0] == text[stat[1]]:
                print(f">instruction: {instruction}")
                if instruction[2] == "MVR":
                    self.state.append((instruction[1], stat[1] + 1))
                    print(f">>appending: {(instruction[1], stat[1] + 1)}", end="\n\n")
        print("----------------------")            
                

    def iterateText(self, text):
        while True:
            try:
                s = self.state.pop()
                print(f"     > taking state : {s}")
                self.move(self.mess["instructions"], text, s)
            except:
                if self.is_accepting_state(s[0]):
                    return True
                elif self.state.__len__() == 0:
                    return False



aut1 = automaton("data.2.json")

print(aut1.is_in_alphabet("0"))
print(aut1.is_in_alphabet("a"))
text = "aaabba"
print(f"iteratin {text}")
print(aut1.iterateText("aaabba"))
