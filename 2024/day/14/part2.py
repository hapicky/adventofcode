from sys import stdin
import os

# tiles
H = 103
W = 101

# input
positions = []
velocities = []

for line in stdin:
    line = line.rstrip('\n')

    p, v = line.split()
    px, py = map(int, p[2:].split(','))
    vx, vy = map(int, v[2:].split(','))

    positions.append((px, py))
    velocities.append((vx, vy))

# teleport
def teleport(positions, velocities):
    new_positions = [None] * len(positions)

    for i, p in enumerate(positions):
        nx = (p[0] + velocities[i][0]) % W
        ny = (p[1] + velocities[i][1]) % H
        new_positions[i] = (nx, ny)

    return new_positions

# output picture
for i in range(10000):
    positions = teleport(positions, velocities)

    tiles = [[0] * W for _ in range(H)]
    for x, y in positions:
        tiles[y][x] += 1

    dir_path = './pictures/' + str(((i+1) // 1000) * 1000)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    with open(dir_path + '/' + str(i+1) + '.txt', mode='w') as f:
        for r in tiles:
            line = ''.join([' ' if c == 0 else '*' for c in r]) + '\n'
            f.write(line)
