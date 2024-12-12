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

# count sides
sides = defaultdict(set)

# prior left and up
dir_sides = [
    (-1, 0, 'L'),
    (0, -1, 'U'),
    (1, 0, 'R'),
    (0, 1, 'D')
]

for y in range(H):
    for x in range(W):
        rep = find_parent(x, y)

        for dx, dy, side in dir_sides:
            nx = x + dx
            ny = y + dy

            side_key = '_'.join([str(x), str(y), side])

            if side == 'R' or side == 'L':
                prev_side_key = '_'.join([str(x), str(y-1), side])
            else:
                prev_side_key = '_'.join([str(x-1), str(y), side])

            if nx < 0 or ny < 0 or nx >= W or ny >= H:
                sides[rep].add(side_key)
                # remove the preceding edge
                sides[rep].discard(prev_side_key)
            elif rows[y][x] != rows[ny][nx]:
                sides[rep].add(side_key)
                # remove the preceding edge
                sides[rep].discard(prev_side_key)


ans = 0
for rep in rep_points:
    if rep in sizes:
        ans += sizes[rep] * len(sides[rep])
    else:
        ans += len(sides[rep])

print(ans)
