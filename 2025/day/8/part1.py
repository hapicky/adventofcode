from math import prod
from sys import stdin

# input junctions
junctions = []

for line in stdin:
    junction = tuple(map(int, line.split(',')))
    junctions.append(junction)

# calculate distance
def distance_sq(junction1, junction2):
    return (junction1[0] - junction2[0]) ** 2 + (junction1[1] - junction2[1]) ** 2 + (junction1[2] - junction2[2]) ** 2

distances = []
for i in range(len(junctions) - 1):
    for j in range(i + 1, len(junctions)):
        dist_sq = distance_sq(junctions[i], junctions[j])
        distances.append((dist_sq, i, j))

distances.sort()


# Union-Find
parents = [None] * len(junctions)
circuits_size = [1] * len(junctions)

def find_root(i):
    root = i
    while parents[root] is not None:
        root = parents[root]

    return root

# connect junctions
PAIRS = 10 if len(junctions) == 20 else 1000

for _, j1, j2 in distances[:PAIRS]:
    j1_root = find_root(j1)
    j2_root = find_root(j2)

    if j1_root == j2_root:
        continue

    size1 = circuits_size[j1_root]
    size2 = circuits_size[j2_root]

    if size1 < size2:
        parents[j1_root] = j2_root
        circuits_size[j2_root] += size1
    else:
        parents[j2_root] = j1_root
        circuits_size[j1_root] += size2

ans = prod(sorted(circuits_size)[-3:])
print(ans)
