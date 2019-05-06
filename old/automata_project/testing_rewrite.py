import automata as automata

aut2 = automata.automaton("rewriting.json")
#aut2.print_instructions()
text = "001010101010101"
aut2.iterateText(text)