import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    ranges = [r.split("-") for r in file.readline().strip().split(",")]

total = 0
for start, end in ranges:
    if len(start) % 2 == 1:
        start = "1" + "0" * len(start)
    if len(end) % 2 == 1:
        end = "9" * (len(end) - 1)
    half_start = start[:len(start) // 2]
    half_end = end[:len(end) // 2]
    for half in range(int(half_start), int(half_end) + 1):
        invalid = int(str(half) + str(half))
        if invalid >= int(start) and invalid <= int(end):
            printd(start, end, invalid)
            total += invalid
print(total)
