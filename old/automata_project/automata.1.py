import itertools
import json

class status:
    def __init__(self, state, position, num_text):
        self.state, self.position, self.num_text = state, position, num_text
    

    def __str__(self):
        return f"state: {self.state}, position: {self.position}, num_text: {self.num_text} "


class automaton:
    def __init__(self, file, size_of_window = 1):
        with open(file, mode='r') as inp:
            self.mess = json.load(inp)
        self.size_of_window = size_of_window
        self.stats = [ status(self.mess["s0"][0], self.mess["s0"][1], 0)]


    def is_in_alphabet(self, ch):
        for i in self.mess["alfabet"]:
            if i == ch:
                return True
        return False


    def is_accepting_state(self, state):
        for i in self.mess["sAcc"]:
            if i == state:
                return True
        return False       


    def __make_instruction(self, instruction, new_state, stat): #beware not functioning for window >1
        if instruction == "MVR":
            s = status(new_state, stat.position + 1, stat.num_text)
            self.stats.append( s)
            return
        elif instruction == "RES":
            s = status(new_state, 0, stat.num_text)
            self.stats.append( s)
            return
        elif instruction == "REM": 
            new_list = list(self.texts[stat.num_text])
            del new_list[stat.position]
            self.texts.append(new_list)

            s = status(new_state, stat.position, len(self.texts) -1)
            self.stats.append(s)
            return
        elif self.is_in_alphabet(instruction):
            new_list = self.texts[stat.num_text].copy()
            new_list[stat.position] = instruction
            self.texts.append(new_list)

            s = status(new_state, stat.position, len(self.texts) -1)
            self.stats.append(s)
            return


    def add_instruction(self, from_state, value, to_state, instruction):
        for i in self.mess["instructions"][from_state][value]:
            if i == [to_state, instruction]:
                return
        self.mess["instructions"][from_state][value].append([to_state, instruction])

    def replace_instructions(self, from_state, value, to_state, instruction):
        self.mess["instructions"][from_state][value] = [[to_state, instruction]]

    def move(self, window, stat):
        posibilites = self.mess["instructions"][stat.state]
        for posibility in posibilites[window]:
            print(f">instruction: {window} -> new_state: {posibility[0]}, instruction: {posibility[1]}  " )
            self.__make_instruction(posibility[1], posibility[0], stat)
        print("----------------------------------", end="\n\n")
            

    def get_window(self, text, position):
        if self.size_of_window == 1:
            return text[position]
        elif self.size_of_window < 1:
            raise IndexError()
        return str(text[position : position + self.size_of_window]) # so it returns something like ["a", "b"]

    def concat_text(self, text):
        newtext = []
        ctr = 0
        strg = ""
        for i in text:
            if i == "[":
                ctr +=1
            elif i == "]":
                ctr -=1
            strg += i
            if ctr == 0:
                newtext.append(strg)
                strg = ""
        if ctr != 0:
            raise ImportWarning("[] are not in pairs")
        return newtext


    def iterateText(self, text):
        self.texts = [self.concat_text(text)]
        print(self.texts[0])
        while True:
            try:
                s = self.stats.pop()
                print(f"     > taking status : {s}")
                window = self.get_window(self.texts[s.num_text], s.position)
                print(f" text: {self.texts[s.num_text]}")
                print(f" window: {window}")
                self.move(window, s)
            except:
                if self.is_accepting_state(s.state):
                    print(f"remaining tuples = {self.stats}")
                    print(f"number of copies of text = {len(self.texts)}")
                    return True
                elif self.stats.__len__() == 0:
                    return False


    def print_instructions(self):
        for state in self.mess["instructions"]:
            print(f"states: {state}: <" , end="")
            for value in self.mess["instructions"][state]:
                print(f" \"{value}\" : [", end = "")
                for instruct in self.mess["instructions"][state][value]:
                    print(f"{instruct}", end = "")
                print("]", end ="")
            print(">")


    def save_instructions(self, to):
        with open(to, "w") as to_file:
            json.dump(self.mess, to_file)  


    def is_deterministic(self):
        for state in self.mess["instructions"]:
            for value in self.mess["instructions"][state]:
                if len(self.mess["instructions"][state][value]) > 1:
                    return False
        return True
    
    def clear(self):
        self.mess = {}

aut1 = automaton("data.json")

aut1.replace_instructions("st0", "b", "st0", "MVR")
aut1.add_instruction("st0", "b", "st0", "MVR")
aut1.clear()
aut1.print_instructions()
aut1.save_instructions("data.1.json")
print(aut1.is_deterministic())
text = "baa[a,b]aba"
print(f"iteratin {text}")
print("---------------------")
print(aut1.iterateText(text))