class player:
    def __init__(self, name):
        self.name = name
    score = 0

    def __repr__(self):
        return f"<Player: {self.name}>"

class edge:
    def __init__(self, fromP, toP, weight):
        



class swiss:
    score = []
    matched = []
    umatched = []
    def new_selection(arr):
        for player in range(len(arr)):
            epsilon = max(self.score)
            for opponent in range(len(arr)):
                if player == opponent: continue
                if opponent in self.matched[player]: 
                    distance = abs(score[player] - score[opponent])
                if distance < epsilon:
                    epsilon = distance

def fillPlayers():
    players = []
    for i in range(16):
        p = player(i)
        players.append(p)
    return players


if __name__ == "__main__":
    box = fillPlayers()
    print(box)

