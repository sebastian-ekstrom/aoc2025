import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

shapes = []
problems = []
line = 0
while line < len(lines):
    if lines[line][-1] == ":":
        shape = set()
        for y in range(3):
            for x in range(3):
                if lines[line + 1 + y][x] == "#":
                    shape.add((x, y))
        shapes.append(shape)
        line += 5
    else:
        tokens = lines[line].split()
        w, h = [int(i) for i in tokens[0][:-1].split("x")]
        problems.append((w, h, [int(i) for i in tokens[1:]]))
        line += 1

total = 0
for x, y, presents in problems:
    size = x * y
    total_shape_size = 0
    for n in range(len(presents)):
        total_shape_size += presents[n] * len(shapes[n])
    printd(size - total_shape_size)
    if size > total_shape_size:
        total += 1
print(total)
