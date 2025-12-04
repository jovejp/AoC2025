import  sys
from time import time

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

# Split the content into two parts based on a double newline
part1 = content.split('\n')
g1 = [[c for c in line] for line in part1]

def count_around_at(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [[0]*cols for _ in range(rows)]
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for x in range(rows):
        for y in range(cols):
            count = 0
            if grid[x][y] == '.':
                result[x][y] = 9
                continue
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '@':
                    count += 1
            result[x][y] = count
    return result


def part1():
    result = count_around_at(g1)
    count = sum(1 for row in result for v in row if v < 4)
    return count


def count_around_at_v2(grid):
    sum_index = 0
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for x in range(rows):
        for y in range(cols):
            count = 0
            if grid[x][y] == '.':
                continue
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '@':
                    count += 1
            if count < 4:
                sum_index += 1
                grid[x][y] = '.'
    return sum_index, grid


def part2():
    result, grid = count_around_at_v2(g1)
    while 1:
        new_result, grid = count_around_at_v2(grid)
        if new_result == 0:
            break
        result += new_result
    return result


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)