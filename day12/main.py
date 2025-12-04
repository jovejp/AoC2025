import  sys
from time import time

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

# Split the content into two parts based on a double newline
part1 = content.split('\n')
g1 = [[c for c in line] for line in part1]


def part1():
    return "part1 not implemented"



def part2():
    return "part2 not implemented"


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)