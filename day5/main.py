import  sys
from time import time

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

# Split the content into two parts based on a double newline
part1, part2 = content.split('\n\n', 1)
g1 = [[int(c) for c in line.split('-')] for line in part1.split('\n')]
g1_sorted = sorted(g1, key=lambda x: x[0])
# print("g1:", g1_sorted)
g2 = [int(line) for line in part2.split('\n')]



def in_g1_ranges(num, g1):
    for start, end in g1:
        if num < start:
            return 0
        if start <= num <= end:
            return 1
    return 0

def part1():
    result = 0
    for i in g2:
        result += in_g1_ranges(i, g1_sorted)
    return result


def count_unique_numbers(g1):
    merged = []
    for start, end in g1:
        if not merged or merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    total = sum(end - start + 1 for start, end in merged)
    return total

def part2():
    total = count_unique_numbers(g1_sorted)
    return total


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)