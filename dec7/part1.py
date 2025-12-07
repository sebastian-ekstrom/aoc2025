import sys

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

splits = 0
beams = {grid[0].find("S")}
for y in range(1, len(grid)):
    next_beams = set()
    for x in beams:
        if grid[y][x] == "^":
            next_beams.add(x-1)
            next_beams.add(x+1)
            splits += 1
        else:
            next_beams.add(x)
    beams = next_beams
print(splits)
