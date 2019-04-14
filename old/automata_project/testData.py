import json

data = {}

with open("data.json") as file:
    data = json.load(file)


for i in data.values():
    print(i)