import json

with open("moviesData.json") as jsonFile:
    data = json.load(jsonFile)

print(json.dumps(data, indent=2, sort_keys=True))

for x in data:
    if x["genero"] == "Action":
        print(x["nombre"])
