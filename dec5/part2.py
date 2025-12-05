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
        start, end = [int(i) for i in line.split("-")]
        for i in range(len(ranges)):
            start2, end2 = ranges[i]
            if start >= start2 and end <= end2:
                start = -1
                end = -1
                break
            elif start <= start2 and end >= end2:
                ranges[i] = (-1, -1)
            elif end >= start2 and end <= end2:
                end = start2 - 1
            elif start >= start2 and start <= end2:
                start = end2 + 1
        if start <= end:
            ranges.append((start, end))

total = 0
for start, end in ranges:
    if start < 0:
        continue
    total += end - start + 1

print(total)
