import  sys
from time import time

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()
part1 = content.split(',')
g1 = [[item.strip() for item in line.strip().split('-')] for line in part1]
# print(g1)

valid_id_part1 = []

def get_all_valid(start, end):
    nss = str(start)
    nes = str(end)
    ls = len(nss)
    le = len(nes)

    if ls % 2 != 0:
        ls += 1
        nss = "1" + "0" * (ls - 1)
    hs = ls // 2
    if nss[:hs] >= nss[hs:]:
        nhs =  int(nss[:hs])
    else:
        nhs = int(nss[:hs]) + 1

    if le % 2 != 0:
        le -= 1
        nes = "9" * le
    he = le // 2
    if nes[:he] <= nes[he:]:
        mhe = int(nes[:he])
    else:
        mhe = int(nes[:he]) - 1

    if ls == le:
        # print(f"normal case: {nhs} to {mhe}")
        valid_id_part1.extend(range(nhs, mhe + 1))
    # elif ls > le:
    #     print(f"normal case, no valid numbers")
    # else:
    #     print("special case, warning!")
    #     print(start, end, ls, le, nhs, mhe)


def part1():
    for item in g1:
        start = int(item[0])
        end = int(item[1])
        get_all_valid(start, end )
    # print(valid_id_part1)
    return sum(int(str(s) * 2) for s in valid_id_part1)



def get_all_valid_part2(start, end, i, valid_id_item):
    nss = str(start)
    nes = str(end)
    ls = len(nss)
    le = len(nes)

    if ls % i == 0 or (ls + 1) % i == 0:
        pass
    else:
        return
    if le % i == 0 or (le - 1) % i == 0:
        pass
    else:
        return

    if ls % i != 0:
        ls += 1
        nss = "1" + "0" * (ls - 1)
    hs = ls // i

    if int(nss[:hs]*i) >= start:
        nhs =  int(nss[:hs])
    else:
        nhs = int(nss[:hs]) + 1

    if le % i != 0:
        le -= 1
        nes = "9" * le
    he = le // i
    if int(nes[:he]*i) <= end:
        mhe = int(nes[:he])
    else:
        mhe = int(nes[:he]) - 1

    if ls == le:
        # print(f"normal case: {nhs} to {mhe}")
        for s in range(nhs, mhe + 1):
            valid_id_item.add(int(str(s) * i))

valid_id_part2 = []
def part2():
    for item in g1:
        start = int(item[0])
        end = int(item[1])
        valid_id_item = set()
        for i in range(2, len(str(end)) +1):
            get_all_valid_part2(start, end, i, valid_id_item)
        valid_id_part2.extend(valid_id_item)
    return sum(valid_id_part2)

t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)