import sys
from collections import defaultdict

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

beams = defaultdict(int)
beams[grid[0].find("S")] = 1
for y in range(1, len(grid)):
    next_beams = defaultdict(int)
    for x, count in beams.items():
        if grid[y][x] == "^":
            next_beams[x-1] += count
            next_beams[x+1] += count
        else:
            next_beams[x] += count
    beams = next_beams
print(sum(beams.values()))
