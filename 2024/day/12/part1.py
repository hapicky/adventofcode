from sys import stdin
from collections import defaultdict

# input
rows = []

for line in stdin:
    row = list(line.rstrip('\n'))
    rows.append(row)

# garden size
H = len(rows)
W = len(rows[0])

# Union-Find
parents = dict()
sizes = dict()

def find_parent(x, y):
    parent = (x, y)
    while parent in parents:
        parent = parents[parent]
    
    return parent

directions = [
    (1, 0),
    (0, 1)
]

for y in range(H):
    for x in range(W):
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx == W or ny == H:
                continue

            if rows[y][x] != rows[ny][nx]:
                continue

            parent = find_parent(x, y)
            n_parent = find_parent(nx, ny)

            if parent == n_parent:
                continue

            size = sizes.get(parent, 1)
            n_size = sizes.get(n_parent, 1)

            if size < n_size:
                parents[parent] = n_parent
                sizes[n_parent] = size + n_size
            else:
                parents[n_parent] = parent
                sizes[parent] = size + n_size

# representative points
rep_points = set()
for y in range(H):
    for x in range(W):
        rep_points.add(find_parent(x, y))

# count perimeters
perimeters = defaultdict(int)

directions.extend([
    (-1, 0),
    (0, -1)
])

for y in range(H):
    for x in range(W):
        perimeter = 0
        rep = find_parent(x, y)

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= W or ny >= H:
                perimeter += 1
            elif rows[y][x] != rows[ny][nx]:
                perimeter += 1
        
        perimeters[rep] += perimeter


ans = 0
for rep in rep_points:
    if rep in sizes:
        ans += sizes[rep] * perimeters[rep]
    else:
        ans += perimeters[rep]

print(ans)
