from collections import ChainMap


population = {
    "italy": 60,
    "japan": 127,
    "uk": 65
}

changes = dict()
editable = ChainMap(changes, population)

print(f"Before update: {editable['japan']}")

editable["japan"] += 1
print(f"Updated population: {editable['japan']}")
print(f"Original population: {population['japan']}")

print(f"Changes: {changes.keys()}")
print(f"Did not changed: {population.keys() - changes.keys()}")
