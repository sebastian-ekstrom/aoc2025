import sys

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

ranges = []
ingredients = []

for line in lines:
    if "-" in line:
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    elif len(line) > 0:
        ingredients.append(int(line))

total = 0
for ingredient in ingredients:
    for start, end in ranges:
        if ingredient >= start and ingredient <= end:
            total += 1
            break

print(total)
