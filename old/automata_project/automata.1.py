import itertools
import json

class automaton:
    # state - list of tuples (state, position)
    def __init__(self, file):
        with open(file, mode='r') as inp:
            self.mess = json.load(inp)
        print(self.mess["instructions"]["st1"]['a'])
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
                    self.state.append((instruction[1], stat[1][0] + 1))
                    print(f">>appending: {(instruction[1], stat[1][0] + 1)}", end="\n\n")
                # rewrite petr somal 
        print("----------------------")            


    def move3(self, text, stat):
        # mk seznam objektu-stringu
        posibilites = self.mess["instructions"][stat[0]]
        window = self.get_window(text, stat[1])
        for inst in posibilites[window]:
            print(f">instruction: {window} -> {inst}")
            if inst[1] == "MVR":
                self.state.append((inst[0], [stat[1][0] + 1]))
                print(f">>appending: {(inst[0], [stat[1][0] + 1])}", end="\n\n")
        print("----------------------")


    def get_window(self, text, tuple_of_size):
        if len(tuple_of_size) == 1:
            return text[tuple_of_size[0]]
        elif len(tuple_of_size) > 1:
            return text[tuple_of_size[0]:tuple_of_size[1]]
        raise IndexError()

        

    def iterateText(self, text):
        while True:
            try:
                s = self.state.pop()
                print(f"     > taking state : {s}")
                self.move3(text, s)
                #self.move(self.mess["instructions"], text, s)
            except:
                if self.is_accepting_state(s[0]):
                    print(f"remaining tuples = {self.state}")
                    return True
                elif self.state.__len__() == 0:
                    return False



aut1 = automaton("data.3.json")

#aut1.add_instruction("x,y,z : d(q,[x,y,z]) -> (q,[x,y]) ")
print(aut1.is_in_alphabet("0"))
print(aut1.is_in_alphabet("a"))
text = "baaababa"
print(f"iteratin {text}")
print("---------------------")
print(aut1.iterateText(text))