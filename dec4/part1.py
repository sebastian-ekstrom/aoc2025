import sys

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def get_from_grid(grid, x, y):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return None
    return grid[y][x]

def count_neighbors(grid, x, y, target):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if get_from_grid(grid, x + dx, y + dy) == target:
                count += 1
    return count

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

total = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "@" and count_neighbors(grid, x, y, "@") < 4:
            total += 1
print(total)
