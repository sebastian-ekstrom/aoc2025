import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    banks = [line.strip() for line in file]

total = 0
for bank in banks:
    char1 = max(bank[:-1])
    char2 = max(bank[bank.find(char1) + 1:])
    printd(char1 + char2)
    total += int(char1 + char2)

print(total)
