import  sys
from collections import defaultdict
import re

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()
part1 = content.split('\n')
g1 = [[int(c) for c in line] for line in part1]
# print(g1)

def find_max_positions(arr):
    first_max_idx = arr.index(max(arr[:-1]))
    second_max_idx = first_max_idx + 1 + arr[first_max_idx+1:].index(max(arr[first_max_idx+1:]))
    return arr[first_max_idx], arr[second_max_idx]

def part1():
    result = 0
    for item in g1:
        max1, max2 = find_max_positions(item)
        # print(f"Max values: {max1*10+max2}")
        result += max1*10 + max2
    return result



def find_max_positions_v2(arr):
    n = len(arr)
    max_indices = []
    start = 0
    for i in range(12):
        end = n - (12 - i)
        max_idx = arr.index(max(arr[start:end+1]), start, end+1)
        max_indices.append(arr[max_idx])
        start = max_idx + 1
    # 12個の最大値を連結して数字にする
    return int(''.join(map(str, max_indices)))

def part2():
    result = 0
    for item in g1:
        max1 = find_max_positions_v2(item)
        # print(f"Max values: {max1}")
        result += max1
    return result


print("Part one:", part1())
print("Part two:", part2())