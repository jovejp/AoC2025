import  sys
from time import time
from functools import reduce
import operator

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

g0= content.splitlines()[:-1]
# print("g0:", g0)
g1= [[int(item) for item in line.split() ] for line in content.splitlines()[:-1]]
g2 = [ item for item in content.splitlines()[-1].split()]
ops = {"+": operator.add, "*": operator.mul}





def part1():
    # print(sum(reduce(ops[col[-1]], col[:-1]) for col in zip(*rows)))
    total = 0
    for idx, col in enumerate(zip(*g1)):
       # print("col:", col, "op:", idx)
       total += reduce(ops[g2[idx]], col)
    return total


def part2():
    # rotate g0 90 degrees clockwise
    rotated = list(zip(*g0))[::-1]

    result = []
    current_group = []

    for row in rotated:
        combined = ''.join(row).strip()  # combine and strip spaces
        if combined:  # if not a space line
            try:
                current_group.append(int(combined))  # convert to int and add to current group
            except ValueError:
                print(f"Error when convert to int: {combined}")
        elif current_group:
            result.append(current_group)
            current_group = []
        else:
            print("error: empty line encountered with no current group")

    # last group
    if current_group:
        result.append(current_group)
    # print("Result:", result)

    total = 0
    idx_op = len(g2) - 1
    for idx, col in enumerate(result):
        # print("col:", col, "op:", idx)
        total += reduce(ops[g2[idx_op-idx]], col)

    return total


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)