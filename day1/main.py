import  sys
from collections import defaultdict
import re

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

# Split the content into two parts based on a double newline
part1, part2 = content.split('\n\n', 1)
# print(part1)
# print(part2)

# Process part1 into a list of lists, splitting each line by ':' and stripping whitespace
g1 = [[item.strip() for item in line.strip().split(':')] for line in part1.split('\n')]
# print(g1)

base_cached_dict = defaultdict(int)

for item in g1:
    if item[0] not in base_cached_dict:
        base_cached_dict[item[0]] = int(item[1])

# Process part2 into a list of lists, splitting each line by whitespace or '->' and stripping whitespace
g2 = [[item.strip() for item in re.split(r'\s+|->', line) if item.strip()] for line in part2.split('\n')]
print(g2)



def part1():
    return "part1 result"




def part2():
    return "part2 result"




print("Part one:", part1())
print("Part two:", part2())