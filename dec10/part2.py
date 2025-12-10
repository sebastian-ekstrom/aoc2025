import sys
from z3 import *

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

machines = []
for line in lines:
    tokens = line.split()
    target = [int(i) for i in tokens[-1][1:-1].split(",")]
    buttons = []
    for token in tokens[1:-1]:
        buttons.append(set(int(i) for i in token[1:-1].split(",")))
    machines.append((target, buttons))

total = 0
for target, buttons in machines:
    opt = Optimize()
    X = [Int(f"x{i}") for i in range(len(buttons))]
    presses = Int("presses")
    for x in X:
        opt.add(x >= 0)
    for n in range(len(target)):
        opt.add(sum([X[i] for i in range(len(buttons)) if n in buttons[i]]) == target[n])
    opt.add(presses == sum(X))
    minimum = opt.minimize(presses)
    opt.check()
    printd(opt.model())
    printd(opt.model()[presses])
    total += opt.model()[presses]
print(simplify(total))
