import sys
from math import prod

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip().split() for line in file]

for y in range(len(grid) - 1):
    for x in range(len(grid[y])):
        grid[y][x] = int(grid[y][x])

total = 0
for x in range(len(grid[0])):
    printd([grid[y][x] for y in range(0, len(grid))])
    if grid[-1][x] == "+":
        total += sum([grid[y][x] for y in range(0, len(grid) - 1)])
    else:
        total += prod([grid[y][x] for y in range(0, len(grid) - 1)])
print(total)
