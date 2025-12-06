import sys
from math import prod

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip("\n") for line in file]

separators = []
for x in range(min([len(line) for line in lines])):
    if all([line[x] == " " for line in lines]):
        separators.append(x)
printd(separators)

problems = []
x = 0
for s in separators:
    problems.append([line[x:s] for line in lines])
    x = s + 1
problems.append([line[x:] for line in lines])

total = 0
for problem in problems:
    printd(problem)
    numbers = []
    for x in range(max(len(line) for line in problem)):
        number_str = ""
        for y in range(len(problem) - 1):
            if x < len(problem[y]):
                number_str += problem[y][x]
        numbers.append(int(number_str.strip()))
    printd(numbers)
    if problem[-1][0] == "+":
        total += sum(numbers)
    else:
        total += prod(numbers)
print(total)
