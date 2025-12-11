import sys
from collections import defaultdict

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

outputs = defaultdict(list)

for line in lines:
    tokens = line.split()
    name = tokens[0][:-1]
    outputs[name] += tokens[1:]

paths = 0
current_nodes = defaultdict(int)
current_nodes["you"] = 1
while len(current_nodes) > 0:
    next_nodes = defaultdict(int)
    for node, nbr in current_nodes.items():
        for output in outputs[node]:
            if output == "out":
                paths += nbr
            else:
                next_nodes[output] += nbr
    current_nodes = next_nodes
print(paths)
