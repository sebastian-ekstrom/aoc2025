import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    banks = [line.strip() for line in file]

total = 0
nbr_chars = 12
for bank in banks:
    chars = ""
    index = 0
    for i in range(nbr_chars):
        printd(index, bank)
        if i == nbr_chars - 1:
            char = max(bank[index:])
        else:
            char = max(bank[index:-nbr_chars+i+1])
        index = bank.find(char, index) + 1
        printd(char)
        chars += char
    printd(chars)
    total += int(chars)

print(total)
