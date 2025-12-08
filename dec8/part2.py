import sys
from math import sqrt
import heapq
from collections import defaultdict

debug = False
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

heapq.heapify(edges)

neighbors = defaultdict(set)

while True:
    _, n1, n2 = heapq.heappop(edges)
    printd(n1, n2, nodes[n1], nodes[n2])
    neighbors[n1].add(n2)
    neighbors[n2].add(n1)

    visited = {0}
    to_visit = neighbors[0]
    while len(to_visit) > 0:
        next_visit = set()
        for n in to_visit:
            if n in visited:
                continue
            visited.add(n)
            next_visit |= neighbors[n]
        to_visit = next_visit
    if len(visited) == len(nodes):
        print(nodes[n1][0] * nodes[n2][0])
        break
