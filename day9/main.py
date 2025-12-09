import  sys
from time import time
from itertools import combinations
from collections import defaultdict

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

# Split the content into two parts based on a double newline
part1 = content.split('\n')
g1 = [[int(c) for c in line.split(',')] for line in part1]
# print(g1)
g1_swapped = [[b, a] for a, b in g1]
g1_sorted = sorted(g1_swapped, key=lambda x: x[0])
# print(g1_sorted)
row_dict = defaultdict(list)
for row, col in g1_sorted:
    row_dict[row].append(col)
min_max_per_row= defaultdict(list)

prev_min, prev_max = None, None
pre_row = None
for row in sorted(row_dict):
    cols = row_dict[row]
    # print("Row:", row, "Cols:", cols, "Prev min:", prev_min, "Prev max:", prev_max, "pre_row:", pre_row)
    if pre_row and row == pre_row + 1:
        print("Unsupported cases!!!!")
    if cols:
        min_col, max_col = min(cols), max(cols)
        if pre_row is None:
            min_max_per_row[row] = [min_col, max_col]
            prev_min, prev_max = min_max_per_row[row]
        else:
            new_min = min(prev_min, min_col)
            new_max = max(prev_max, max_col)
            min_max_per_row[row] = [new_min, new_max]
            if prev_min == max_col or prev_max == min_col:
                min_max_per_row[row - 1] = [prev_min, prev_max]
                prev_min, prev_max = min_max_per_row[row]
            elif prev_min == min_col and prev_max == max_col:
                print("end, no change needed")
            elif prev_min == min_col:
                next_min = min(prev_max, max_col)
                next_max = max(prev_max, max_col)
                min_max_per_row[row+1] = [next_min, next_max]
                prev_min, prev_max = next_min, next_max
            elif prev_max == max_col:
                next_min = min(prev_min, min_col)
                next_max = max(prev_min, min_col)
                min_max_per_row[row+1] = [next_min, next_max]
                prev_min, prev_max = next_min, next_max
            else:
                prev_min, prev_max = min_max_per_row[row]
    else:
        print("unexpected case!!!!, no cols found")
    pre_row = row
sorted_min_max_per_row = sorted(min_max_per_row.items())
# print(sorted_min_max_per_row)

def part1():
    max_val = 0
    max_pairs = []
    for (x, y), (x1, y1) in combinations(g1, 2):
        val = (abs(x1 - x) + 1) * (abs(y1 - y) + 1)
        if val > max_val:
            max_val = val
            max_pairs = [((x, y), (x1, y1))]
        elif val == max_val:
            max_pairs.append(((x, y), (x1, y1)))
    print(max_pairs)
    return max_val


def part2():
    max_area = 0
    max_pair = None
    for (x, y), (x1, y1) in combinations(g1_sorted, 2):
        continue_flag = False
        row_start, row_end = min(x, x1), max(x, x1)
        col_start, col_end = min(y, y1), max(y, y1)
        filtered = [(row, vals) for row, vals in sorted_min_max_per_row if row_start <= row <= row_end]
        for i, item in filtered:
            blocked_min, blocked_max = item
            if blocked_min > col_start or blocked_max < col_end:
                continue_flag = True
                break
        if continue_flag:
            continue
        area = (abs(row_end - row_start) + 1) * (abs(col_end - col_start) + 1)
        if area > max_area:
            max_area = area
            max_pair = ((x, y), (x1, y1))

    print("Max pair:", max_pair)
    print("Max area:", max_area)
    return max_area


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)