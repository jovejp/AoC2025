import  sys

filename = "sample.txt" if len(sys.argv) == 1 else "input.txt"

with open(filename) as file:
    contents = file.read()
all_blocks = contents.split('\n\n')
g1 = all_blocks[:-1]
g2 = all_blocks[-1]

block_sizes = [line.count("#")  for line in g1]
square_area = [ int(part.split(':')[0].split('x')[0]) * int(part.split(':')[0].split('x')[1]) for part in g2.splitlines()]
combined_requirements = [[[index, int(num)] for index, num in enumerate(part.split(':')[1].split())] for part in g2.splitlines() ]
combined_aras = [sum([(block_sizes[item[0]] * item[1]) for item in line]) for line in combined_requirements]
# print(square_area)
# print(combined_aras)
# the solution is not accurate, but the result seems correct.
# example used is still wrong.
# no idea for good solution.
result = sum(1 if square_area[x] > combined_aras[x] else 0 for x in range(len(square_area)))
print(result)