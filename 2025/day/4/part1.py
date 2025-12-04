from sys import stdin

# input grid
rows = []
for line in stdin:
    rows.append(line.rstrip())

# count the adjacent roll papers
count = [[0] * (len(rows[0]) + 2) for _ in range(len(rows) + 2)]

adjacents = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]

for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col != '@':
            continue

        for px, py in adjacents:
            nx = x + px + 1
            ny = y + py + 1
            count[ny][nx] += 1

# count accessible papers
ans = 0
for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col == '@' and count[y+1][x+1] < 4:
            ans += 1

print(ans)
