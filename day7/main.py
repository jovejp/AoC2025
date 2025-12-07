import  sys
from collections import defaultdict
from time import time

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

# Split the content into two parts based on a double newline
part1 = content.split('\n')
g1 = [[c for c in line] for line in part1]


def find_coordinates_and_process(grid):
    # 找到'S'的初始坐标
    start_x, start_y = next((x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == 'S')
    # print("Start coordinates:", (start_x, start_y))
    history = set()
    current_set = {(start_x, start_y)}
    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1
    # 循环处理当前坐标集合
    while current_set:
        next_set = set()
        for x, y in current_set:
            if x + 1 <= max_x and (x + 1, y) not in history:  # 检查是否已经访问过
                if grid[x + 1][y] == '.':
                    next_set.add((x + 1, y))
                elif grid[x + 1][y] == '^':
                    history.add((x + 1, y))
                    if y - 1 >= 0:
                        next_set.add((x + 1, y - 1))
                    if y + 1 <= max_y:
                        next_set.add((x + 1, y + 1))
        current_set = next_set
        # print(history)
    # print("History of visited coordinates:", history)

    # 返回历史记录集合的数量
    return len(history)

def part1():
    return find_coordinates_and_process(g1)





def find_coordinates_and_process_v2(grid):
    # 找到'S'的初始坐标
    start_x, start_y = next((x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == 'S')
    # print("Start coordinates:", (start_x, start_y))
    history = set()
    cost = defaultdict(int)
    cost[(start_x, start_y)] = 1
    # print("Initial cost map:", cost)
    result_set = defaultdict(int)
    current_set = {(start_x, start_y)}
    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1
    while current_set:
        next_set = set()
        for x, y in current_set:           
            if x + 1 <= max_x:  # 检查是否已经访问过
                if grid[x + 1][y] == '.':
                    next_set.add((x + 1, y))
                    cost[(x + 1, y)] += cost[(x, y)]
                elif grid[x + 1][y] == '^':
                    history.add((x + 1, y))
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
                # print("Reached bottom edge at:", (x, y))
                # print(cost[(x, y)])
                result_set[(x, y)] = cost[(x, y)]
        # print("Current cost map:", cost)
        # print("Current set:", current_set)
        # print("Result set so far:", result_set)
        # print("next set:", next_set)
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