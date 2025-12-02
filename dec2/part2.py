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
    for i in range(int(start), int(end) + 1):
        string = str(i)
        for length in range(1, len(string) // 2 + 1):
            if len(string) % length != 0:
                continue
            if string == string[:length] * (len(string) // length):
                total += i
                printd(i)
                break
print(total)
