import  sys
from time import time
from functools import reduce
import operator
from itertools import groupby

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

g0= content.splitlines()[:-1]
# print("g0:", g0)
g1= [[int(item) for item in line.split() ] for line in content.splitlines()[:-1]]
g2 = [ item for item in content.splitlines()[-1].split()]
ops = {"+": operator.add, "*": operator.mul}





def part1():
    # total = 0
    # for col in zip(g2,*g1):
    #     total += reduce(ops[col[0]], col[1:])
    # return total
    return sum(reduce(ops[col[0]], col[1:]) for col in zip(g2,*g1))


def part2():
    # rotate g0 90 degrees clockwise
    rotated = list(zip(*g0))[::-1]
    result = []
    for key, group in groupby(rotated, key=lambda row: ''.join(row).strip() != ''):
        if key:  
            result.append([int(''.join(row).strip()) for row in group if ''.join(row).strip().isdigit()])    
    g2_r = g2[::-1]
    return sum(reduce(ops[g2_r[idx]], col) for idx, col in enumerate(result))


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)