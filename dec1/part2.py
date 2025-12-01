import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    turns = [line.strip() for line in file]

pos = 50
total = 0
for turn in turns:
    printd(f'pos = {pos}, total = {total}')
    printd(turn)
    if turn[0] == "R":
        pos += int(turn[1:])
        if pos >= 100:
            total += pos // 100
            pos %= 100
    else:
        last_pos = pos
        pos -= int(turn[1:])
        if pos <= 0:
            total += -pos // 100 + 1
            pos %= 100
            if last_pos == 0:
                total -= 1

print(f'pos = {pos}, total = {total}')
