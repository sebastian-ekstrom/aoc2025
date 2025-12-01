import sys

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    turns = [line.strip() for line in file]

pos = 50
total = 0
for turn in turns:
    if turn[0] == "R":
        pos = (pos + int(turn[1:])) % 100
    else:
        pos = (pos - int(turn[1:])) % 100
    if pos == 0:
        total += 1
print(total)
