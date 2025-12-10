from collections import defaultdict
from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 8)

# input red tiles
red_tiles = []
red_tiles_at_x = defaultdict(list)
red_tiles_at_y = defaultdict(list)

for line in stdin:
    x, y = map(int, line.split(','))

    red_tiles.append((x, y))
    red_tiles_at_x[x].append(y)
    red_tiles_at_y[y].append(x)

red_x = sorted(red_tiles_at_x.keys())
red_y = sorted(red_tiles_at_y.keys())


# create a scaled-down tile map
WIDTH = len(red_x) * 2 + 1
HEIGHT = len(red_y) * 2 + 1

tiles = [['.'] * WIDTH for _ in range(HEIGHT)]

for y in red_y:
    x1, x2 = sorted(red_tiles_at_y[y])
    x1_pos = red_x.index(x1) * 2 + 1
    x2_pos = red_x.index(x2) * 2 + 1
    y_pos = red_y.index(y) * 2 + 1

    # Red
    tiles[y_pos][x1_pos] = '#'
    tiles[y_pos][x2_pos] = '#'

    # Green
    for x_pos in range(x1_pos + 1, x2_pos):
        tiles[y_pos][x_pos] = 'X'

for x in red_x:
    y1, y2 = sorted(red_tiles_at_x[x])
    y1_pos = red_y.index(y1) * 2 + 1
    y2_pos = red_y.index(y2) * 2 + 1
    x_pos = red_x.index(x) * 2 + 1

    # Green
    for y_pos in range(y1_pos + 1, y2_pos):
        tiles[y_pos][x_pos] = 'X'


# make inside green
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def make_green(x, y):
    if tiles[y][x] != '.':
        return

    tiles[y][x] = 'X'

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        make_green(nx, ny)

top_y = red_y[0]
top_left = sorted(red_tiles_at_y[top_y])[0]
x_pos = red_x.index(top_left) * 2 + 2
y_pos = 2

make_green(x_pos, y_pos)


# calculate largest area
largest_area = 0

for i in range(len(red_tiles) - 1):
    for j in range(i + 1, len(red_tiles)):
        x1, x2 = sorted([red_tiles[i][0], red_tiles[j][0]])
        y1, y2 = sorted([red_tiles[i][1], red_tiles[j][1]])

        x1_pos = red_x.index(x1) * 2 + 1
        x2_pos = red_x.index(x2) * 2 + 1
        y1_pos = red_y.index(y1) * 2 + 1
        y2_pos = red_y.index(y2) * 2 + 1

        valid = True
        for y_pos in range(y1_pos, y2_pos + 1):
            if '.' in tiles[y_pos][x1_pos:x2_pos+1]:
                valid = False
                break

        if valid:
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            largest_area = max(largest_area, area)

print(largest_area)
