import  sys
from collections import defaultdict
from time import time

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

part1 = content.split('\n')
g1 = [[c for c in line] for line in part1]


def find_coordinates_and_process(grid):
    start_x, start_y = next((x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == 'S')
    history = set()
    current_set = {(start_x, start_y)}
    max_x, max_y = len(grid) - 1, len(grid[0]) - 1
    while current_set:
        next_set = set()
        for x, y in current_set:
            if x + 1 <= max_x and (x + 1, y) not in history:  
                if grid[x + 1][y] == '.':
                    next_set.add((x + 1, y))
                elif grid[x + 1][y] == '^':
                    history.add((x + 1, y))
                    if y - 1 >= 0:
                        next_set.add((x + 1, y - 1))
                    if y + 1 <= max_y:
                        next_set.add((x + 1, y + 1))
        current_set = next_set
    return len(history)

def part1():
    return find_coordinates_and_process(g1)

def find_coordinates_and_process_v2(grid):
    start_x, start_y = next((x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == 'S')
    cost = defaultdict(int)
    cost[(start_x, start_y)] = 1
    result_set = defaultdict(int)
    current_set = {(start_x, start_y)}
    max_x, max_y = len(grid) - 1, len(grid[0]) - 1
    while current_set:
        next_set = set()
        for x, y in current_set:           
            if x + 1 <= max_x: 
                if grid[x + 1][y] == '.':
                    next_set.add((x + 1, y))
                    cost[(x + 1, y)] += cost[(x, y)]
                elif grid[x + 1][y] == '^':
                    if y - 1 >= 0:
                        next_set.add((x + 1, y - 1))
                        cost[(x + 1, y - 1)] += cost[(x, y)]
                    else:
                        result_set[(x,y)] = cost[(x, y)]
                    if y + 1 <= max_y:
                        next_set.add((x + 1, y + 1))
                        cost[(x + 1, y + 1)] += cost[(x, y)]
                    else:
                        result_set[(x, y)] = cost[(x, y)]
            else:
                result_set[(x, y)] = cost[(x, y)]
        current_set = next_set
    total_sum = sum(result_set.values())
    return total_sum
    



def part2():
    return find_coordinates_and_process_v2(g1)


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)