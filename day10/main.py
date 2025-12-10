from time import time
import re
import itertools
from collections import Counter
from pulp import LpProblem, lpSum, LpVariable, LpMinimize, PULP_CBC_CMD
from z3 import *

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename, encoding="utf-8") as file:
    content = file.read()

# Split the content into two parts based on a double newline
part1 = content.split('\n')
g1 = [[re.search(r'\[.*?\]', line).group(0) if re.search(r'\[.*?\]', line) else None, re.findall(r'\(.*?\)', line), re.search(r'\{.*?\}', line).group(0) if re.search(r'\{.*?\}', line) else None] for line in part1]

def parse_g1(g1):
    result = []
    for square, parens, curly in g1:
        square_list = list(square[1:-1]) if square else None
        parens_list = [list(map(int, re.findall(r'\d+', p))) for p in parens]
        curly_set = list(map(int, re.findall(r'\d+', curly))) if curly else None
        result.append([square_list, parens_list, curly_set])
    return result
result = parse_g1(g1)
# print("Parsed input:", result)

def count_valid_combinations(square_list, parens_list):
    # 1. '#'のインデックス取得
    sharp_indices = [i for i, c in enumerate(square_list) if c == '#']
    sharp_set = set(sharp_indices)
    # print("sharp_set", sharp_set)
    n = len(parens_list)

    # 2. 2個選ぶ組み合わせ
    checked = set()
    for k in range(1, n + 1):
        # print("Checking combinations of size", k)
        for idxs in itertools.combinations_with_replacement(range(n), k):
            # print("Current combination indices:", idxs)
            if tuple(sorted(idxs)) in checked:
                continue
            checked.add(tuple(sorted(idxs)))
            # 選んだ配列を結合
            merged = []
            for i in idxs:
                merged.extend(parens_list[i])
            merged_sorted = sorted(merged)
            odd_indices = [num for num, cnt in Counter(merged_sorted).items() if cnt%2 == 1]
            if set(odd_indices) == sharp_set:
                # print("Combined and sorted list:", merged_sorted)
                # print("Odd indices values:", odd_indices)
                # print("Combination", idxs)
                return len(idxs)
    return None

def part1():
    sum_total = 0
    for square_list, parens_list, curly_set in result:
        if square_list is None or parens_list is None or curly_set is None:
            continue
        # print(square_list, "start processing")
        count = count_valid_combinations(square_list, parens_list)
        # print(square_list, count)
        if count:
            sum_total += count
    # print(sum_total)
    return sum_total


def count_valid_combinations_v2(parens_list, curly_set):
    need_counts = dict(zip(range(len(curly_set)), curly_set))
    total_needed = sum(curly_set)
    lens = [len(p) for p in parens_list if p]
    if not lens:
        return None
    min_len = min(lens)
    max_len = max(lens)
    min_k = math.ceil(total_needed / max_len)
    max_k = total_needed // min_len
    print("Need counts:", need_counts, "Total needed:", total_needed, "Min k:", min_k, "Max k:", max_k)

    n = len(parens_list)
    checked = set()
    for k in range(min_k, max_k + 1):
        for idxs in itertools.combinations_with_replacement(range(n), k):
            key = tuple(sorted(idxs))
            if key in checked:
                continue
            checked.add(key)
            merged = []
            for i in idxs:
                merged.extend(parens_list[i])
            cnt = Counter(merged)
            if all(cnt.get(num, 0) == need_counts[num] for num in need_counts):
                return k
    return None

def count_valid_combinations_v3(parens_list, curly_set):
    # create the problem
    prob = LpProblem("aoc-2025-day-10", LpMinimize)

    # create the variables
    # buttons
    options = len(parens_list)
    press_counts = [
        LpVariable(f"btn-{i}", lowBound=0, cat="Integer") for i in range(options)
    ]

    # objective function
    prob += lpSum(press_counts)
    # constraints
    for num in range(len(curly_set)):
        prob += (
            lpSum(
                press_counts[btn] * parens_list[btn].count(num) for btn in range(options)
            )
            == curly_set[num],
            f"p{num}",
        )
    # solve the problem
    prob.solve(PULP_CBC_CMD(msg=0))
    # print("Status:", prob.status)
    # print("Press counts:", [[v, int(v.varValue)] for v in press_counts])
    total_presses = sum(int(v.varValue) for v in press_counts)
    # print("Total presses:", total_presses)
    return total_presses if total_presses > 0 else None


def count_valid_combinations_v4(parens_list, curly_set):
    # define z3 variables and solver
    n = len(parens_list)
    # z3 variables button press counts variables
    btn_vars = [Int(f'btn_{i}') for i in range(n)]
    s = Optimize()
    # add conditions -1 ,  button press counts >= 0
    for btn in btn_vars:
        s.add(btn >= 0)
    # add conditions button press counts to match curly_set
    for num, target_count in enumerate(curly_set):
        s.add(
            Sum([btn_vars[i] * parens_list[i].count(num) for i in range(n)]) == target_count
        )
    # objective function: minimize total button presses
    s.minimize(Sum(btn_vars))
    # check satisfiability and get result
    if s.check() == sat:
        m = s.model()
        total_presses = sum(m[v].as_long() for v in btn_vars)
        return total_presses if total_presses > 0 else None
    return None

def part2():
    sum_total_2 = 0
    for square_list, parens_list, curly_set in result:
        if square_list is None or parens_list is None or curly_set is None:
            continue
        # print(curly_set, "start processing")
        parens_list_sorted = sorted(parens_list, key=len, reverse=True)
        count = count_valid_combinations_v4(parens_list_sorted, curly_set)
        # print(curly_set, count)
        if count:
            sum_total_2 += count
    # print(sum_total_2)
    return sum_total_2


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)
# z3 - 0.6411697864532471
# pulp - 1.0372817516326904