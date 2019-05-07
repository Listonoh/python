import itertools
import json
import re

class status:
    def __init__(self, state, position, text_version):
        self.state, self.position, self.text_version = state, position, text_version

    def __str__(self):
        return f"state: {self.state}, position: {self.position}, text_version: {self.text_version} "



class automaton:
    def __init__(self, file):
        with open(file, mode='r') as inp:
            self.mess = json.load(inp)
        print(self.mess)
        self.size_of_window = self.mess["size_of_window"]
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
        pos = stat.position
        end_of_pos = self.size_of_window + pos

        if instruction == "MVR":
            s = status(new_state, pos + 1, stat.text_version)
            self.stats.append( s)
            return
        elif instruction == "RES":
            s = status(new_state, 0, stat.text_version)
            self.stats.append( s)
            return
        #matching rewritings for remove use "[]"
        elif re.match(r"^\[.*\]$", instruction):
            new_list = self.texts[stat.text_version].copy()
            new_values = eval(instruction)
            new_list[pos: end_of_pos] = new_values

            self.texts.append(new_list)
            self.paths_of_stats.append(f"{self.paths_of_stats[stat.text_version]} -> \n {new_list}" )
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
            

    def __get_window(self, text, position):
        end_of_pos = position + self.size_of_window
        return str(text[position:end_of_pos])

    def __concat_text(self, text):
        newtext = []
        ctr = 0
        strg = ""
        for i in text:
            if i == "[": ctr +=1
            elif i == "]": ctr -=1
            strg += i
            if ctr == 0:
                newtext.append(strg)
                strg = ""
        if ctr != 0:
            raise ImportWarning("[] are not in pairs")
        return newtext


    def iterateText(self, text):
        self.texts = [self.__concat_text(text)]
        self.paths_of_stats = [ str(self.texts[0]) ]
        print(self.texts[0])
        while True:
            try:
                s = self.stats.pop()
                print(f"     > taking status : {s}")
                window = self.__get_window(self.texts[s.text_version], s.position)
                print(f" text: {self.texts[s.text_version]}")
                print(f" window: {window}")
                self.move(window, s)
            except:
                if self.is_accepting_state(s.state):
                    print(f"remaining tuples = {self.stats}")
                    print(f"number of copies of text = {len(self.texts)}")
                    print(f"path: \n {str(self.paths_of_stats[s.text_version])}")
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
