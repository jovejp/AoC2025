import  sys
from collections import defaultdict
import re

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()
part1 = content


# Process part1 into a list of lists, splitting each line by ':' and stripping whitespace
g1 = [[line.strip()[0], int(line.strip()[1:])] for line in part1.split('\n') if line.strip()]
# print(g1)




def part1():
    sp = 50
    index = 0
    for d in g1:
        d[1] = d[1] % 100
        if d[0] == 'L':
            sp = sp - d[1] + 100 if sp - d[1] < 0 else sp - d[1]
        elif d[0] == 'R':
            sp = sp + d[1] - 100 if sp + d[1] > 99 else sp + d[1]
        else:
            print("Unknown direction", d)
        if sp == 0:
            index += 1
    return index




def part2():
    sp = 50
    index = 0
    for d in g1:
        index += d[1] // 100
        d[1] = d[1] % 100
        if d[0] == 'L':
            if sp - d[1] < 0:
                if sp != 0:
                    index += 1
                sp = sp - d[1] + 100
            else:
                sp = sp - d[1]
        elif d[0] == 'R':
            if sp + d[1] > 99:
                sp = sp + d[1] - 100
                if sp != 0:
                    index += 1
            else:
                sp = sp + d[1]
        else:
            print("Unknown direction", d)
        if sp == 0:
            index += 1
    return index




print("Part one:", part1())
print("Part two:", part2())