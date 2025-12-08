import sys
from math import sqrt
import heapq
from collections import defaultdict

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def dist(n1, n2):
    x1, y1, z1 = n1
    x2, y2, z2 = n2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

filename = sys.argv[1]
with open(filename) as file:
    nodes = [tuple(int(i) for i in line.strip().split(",")) for line in file]

edges = []
for n1 in range(len(nodes) - 1):
    for n2 in range(n1 + 1, len(nodes)):
        edges.append((dist(nodes[n1], nodes[n2]), n1, n2))

sorted_edges = heapq.nsmallest(1000, edges)

neighbors = defaultdict(set)
for _, n1, n2 in sorted_edges:
    neighbors[n1].add(n2)
    neighbors[n2].add(n1)

n_cliques = 0
total = 1
visited = set()
sizes = []
for n in range(len(nodes)):
    if n in visited:
        continue
    n_cliques += 1
    size = 1
    visited.add(n)
    to_visit = neighbors[n]
    while len(to_visit) > 0:
        next_visit = set()
        for n2 in to_visit:
            if n2 in visited:
                continue
            size += 1
            visited.add(n2)
            next_visit |= neighbors[n2]
        to_visit = next_visit
    sizes.append(size)

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
