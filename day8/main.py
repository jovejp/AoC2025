import  sys
from time import time
import math

def calculate_distance(x, y, z, x1, y1, z1):
    return math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2 + (z1 - z) ** 2)


filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    content = file.read()

# Split the content into two parts based on a double newline
part1 = content.split('\n')
g1 = [[int(c) for c in line.split(",")] for line in part1]
max_nodes = len(g1)
print("Total nodes:", max_nodes)
distance_cache = {}


def find_shortest_distance(points):
    distances = []
    for i, (x, y, z) in enumerate(points):
        for j, (x1, y1, z1) in enumerate(points):
            if i < j:  # 避免重复计算
                if (i, j) in distance_cache:
                    distance = distance_cache[(i, j)]
                elif (j, i) in distance_cache:
                    distance = distance_cache[(j, i)]
                else:
                    distance = calculate_distance(x, y, z, x1, y1, z1)
                    distance_cache[(i, j)] = distance
                distances.append(((x, y, z), (x1, y1, z1), distance))
    distances.sort(key=lambda x: x[2])
    return distances

def part1():
    all_path = find_shortest_distance(g1)
    sets_list = []
    i = 1
    for item in all_path:
        point1, point2, dist = item
        found_set = set()
        for s in sets_list:
            if point1 in s or point2 in s:
                found_set.update(s)
                sets_list.remove(s)
        if found_set:
            found_set.add(point1)
            found_set.add(point2)
            sets_list.append(found_set)
        else:
            sets_list.append({point1, point2})
        if i == 1000:
            break
        i += 1
    
    sorted_sets = sorted(sets_list, key=len, reverse=True)
    largest_three = sorted_sets[:3]
    result = 1
    for s in largest_three:
        result *= len(s)
        
    return result



def part2():
    all_cost = find_shortest_distance(g1)
    point1, point2, dist = all_cost[0]
    all_path = all_cost.copy()
    connected_path = set()
    connected_path.add(point1)
    connected_path.add(point2)
    last_node = None

    i = 0
    while len(connected_path) < max_nodes:
        i+=1
        new_path = all_path
        for item in new_path:
            point1, point2, dist = item
            if point1 in connected_path and point2 in connected_path:
                if len(connected_path) == max_nodes:
                    print("warning: Both points in top_points, should not happen!!!!")
                else:
                    all_path.remove(item)
            elif point1 in connected_path or point2 in connected_path:
                if len(connected_path) == max_nodes - 1:
                    print("All points connected.")
                    print("item:", item)
                    if point1 in connected_path:
                        last_node = point2
                    else:
                        last_node = point1
                connected_path.add(point1)
                connected_path.add(point2)
                all_path.remove(item)
                break
            else:
                pass
    print("last_node:", last_node)
    return next((point1[0] * point2[0] for point1, point2, dist in all_cost if last_node in (point1, point2)), None)


t = time()
print("Part one:", part1())
print(time() - t)
t = time()
print("Part two:", part2())
print(time() - t)