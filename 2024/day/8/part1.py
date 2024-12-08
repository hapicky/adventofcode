from sys import stdin
from collections import defaultdict

# input
rows = []
for line in stdin:
    rows.append(list(line.rstrip('\n')))

H = len(rows)
W = len(rows[0])

# antenna
antennas = defaultdict(list)

for y, row in enumerate(rows):
    for x, c in enumerate(row):
        if c != '.':
            antennas[c].append((x, y))

# antinodes
antinodes = set()

for frequency, locations in antennas.items():
    for i in range(len(locations) - 1):
        for j in range(i+1, len(locations)):
            dx = locations[i][0] - locations[j][0]
            dy = locations[i][1] - locations[j][1]

            nx1 = locations[i][0] + dx
            ny1 = locations[i][1] + dy

            if nx1 >= 0 and ny1 >= 0 and nx1 < W and ny1 < H:
                antinodes.add((nx1, ny1))

            nx2 = locations[j][0] - dx
            ny2 = locations[j][1] - dy

            if nx2 >= 0 and ny2 >= 0 and nx2 < W and ny2 < H:
                antinodes.add((nx2, ny2))

ans = len(antinodes)
print(ans)
