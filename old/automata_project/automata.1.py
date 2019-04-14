import itertools
import json

class automaton:
    def __init__(self, file):
        with open(file, mode='r') as inp:
            self.mess = json.load(inp)
        self.state = self.mess["s0"][0] # for deterministic ..


    def is_in_alphabet(self, ch):
        for i in self.mess["alfabet"]:
            if i == ch:
                return True
        return False


    def is_accepting_state(self):
        for i in self.mess["sA"]:
            if i == self.state:
                return True
        return False


    def move(self, mtuple):
        self.state = mtuple[0]
        instruction = mtuple[1]
        if instruction == "MVR":
            self.position += 1

    def iterateText(self, text):
        self.position = 0
        while True:
            try:
                self.mmove(self.mess["instructions"][self.state][text[self.position]])
            except:
                return self.is_accepting_state()



aut1 = automaton("data.2.json")

print(aut1.is_in_alphabet("0"))
print(aut1.is_in_alphabet("a"))
text = "aaabba"
print(f"iteratin {text}")
print(aut1.iterateText("aaabba"))
