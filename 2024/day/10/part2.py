from sys import stdin
from collections import defaultdict

# input
rows = []
trailheads = []

for y, line in enumerate(stdin):
    row = list(map(int, line.rstrip('\n')))
    rows.append(row)

    for x, col in enumerate(row):
        if col == 0:
            trailheads.append((x, y))

# map size
H = len(rows)
W = len(rows[0])

# create graph
graph = defaultdict(list)

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

for y in range(H):
    for x in range(W):
        cur = (x, y)

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= W or ny >= H:
                continue

            if rows[ny][nx] - rows[y][x] == 1:
                graph[cur].append((nx, ny))

def calc_score(x, y):
    if rows[y][x] == 9:
        return 1

    score = 0
    for nx, ny in graph[(x, y)]:
        score += calc_score(nx, ny)

    return score

ans = 0
for sx, sy in trailheads:
    score = calc_score(sx, sy)
    ans += score

print(ans)
