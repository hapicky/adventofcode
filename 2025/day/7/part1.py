from collections import deque
from sys import stdin

# input diagram
rows = []
beams = deque()

for line in stdin:
    row = line.rstrip()
    if 'S' in row:
        beams.append((row.index('S'), 0))

    rows.append(row)

# move beams
splitted = 0
visited = [[False] * len(rows[0]) for _ in range(len(rows))]
visited.append([True] * len(rows[0]))

while beams:
    x, y = beams.popleft()

    ny = y + 1
    if visited[ny][x]:
        continue

    visited[ny][x] = True

    if rows[ny][x] == '^':
        splitted += 1
        beams.append((x - 1, ny))
        beams.append((x + 1, ny))
    else:
        beams.append((x, ny))

print(splitted)
