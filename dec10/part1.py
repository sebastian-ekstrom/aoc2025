import sys
from itertools import combinations

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

machines = []
for line in lines:
    tokens = line.split()
    target = set()
    for i in range(len(tokens[0]) - 2):
        if tokens[0][i+1] == "#":
            target.add(i)
    buttons = []
    for token in tokens[1:-1]:
        buttons.append(set(int(i) for i in token[1:-1].split(",")))
    machines.append((target, buttons))

total = 0
for target, buttons in machines:
    found = False
    for r in range(len(buttons)):
        for possible_buttons in combinations(buttons, r):
            buttons_sum = set()
            for button_set in possible_buttons:
                buttons_sum ^= button_set
            if buttons_sum == target:
                found = True
                total += r
                break
        if found:
            break
    assert(found)

print(total)
