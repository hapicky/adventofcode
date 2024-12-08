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
            antinodes.add(locations[i])
            antinodes.add(locations[j])

            dx = locations[i][0] - locations[j][0]
            dy = locations[i][1] - locations[j][1]

            for sign in [1, -1]:
                nx, ny = locations[i]
                while True:
                    nx += dx * sign
                    ny += dy * sign

                    if nx < 0 or ny < 0 or nx >= W or ny >= H:
                        break

                    antinodes.add((nx, ny))

ans = len(antinodes)
print(ans)
