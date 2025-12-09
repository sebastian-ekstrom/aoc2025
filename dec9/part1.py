import sys

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    tiles = [tuple(int(i) for i in line.strip().split(",")) for line in file]

max_area = 0
for m in range(len(tiles) - 1):
    x1, y1 = tiles[m]
    for n in range(m + 1, len(tiles)):
        x2, y2 = tiles[n]
        max_area = max((abs(x2 - x1) + 1) * (abs(y2 - y1) + 1), max_area)
print(max_area)
