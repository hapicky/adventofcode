from sys import stdin

# tiles
# H = 7
# W = 11
H = 103
W = 101
tiles = [[0] * W for _ in range(H)]

# input and teleport
SECONDS = 100

for line in stdin:
    line = line.rstrip('\n')

    p, v = line.split()
    px, py = map(int, p[2:].split(','))
    vx, vy = map(int, v[2:].split(','))

    x = (px + vx * SECONDS) % W
    y = (py + vy * SECONDS) % H

    tiles[y][x] += 1

# count
H_HALF = (H + 1) // 2
W_HALF = (W + 1) // 2

ans = 1
for i in range(2):
    for j in range(2):
        offset_y = i * H_HALF
        offset_x = j * W_HALF
        robots = 0

        for y in range(offset_y, offset_y + H_HALF - 1):
            row = tiles[y][offset_x:offset_x + W_HALF - 1]
            robots += sum(row)

        ans *= robots

print(ans)
