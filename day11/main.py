import  sys
from time import time
import networkx as nx

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

# Split the content into two parts based on a double newline
part1 = content.split('\n')
g1 =  { line.split(':')[0]: line.split(':')[1].split() for line in part1 if line }



def parse_line(line):
    key, values = line.split(":")
    value_list = values.strip().split()
    return {key.strip(): value_list}
g1 = {k: v for line in part1 if line.strip() for k, v in parse_line(line).items()}
# print("Parsed input:", g1)


def count_paths(g1, start, end):
    if start == end:
        return 1
    if start not in g1:
        return 0
    return sum(count_paths(g1, next_key, end) for next_key in g1[start])

def part1():
    total_paths = count_paths(g1, 'you', 'out')
    return total_paths

cached_counts = {}
def count_paths_v2(start, end, dac, fft):
    if start == end and dac and fft:
        return 1
    elif start == 'dac': dac = True
    elif start == 'fft': fft = True
    elif start not in g1: return 0
    key = (start, dac, fft)
    if key not in cached_counts:
        cached_counts[key] = sum(count_paths_v2(next_key, end, dac, fft) for next_key in g1[start])
    return cached_counts[key]


def part2():
    dac = False
    fft = False
    results = count_paths_v2('svr', 'out', dac, fft )
    print(results)
    return results


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)