from sys import stdin

# input tiles
tiles = []

for line in stdin:
    tile = tuple(map(int, line.split(',')))
    tiles.append(tile)

# calculate largest area
largest_area = 0
for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        w = abs(tiles[i][0] - tiles[j][0]) + 1
        h = abs(tiles[i][1] - tiles[j][1]) + 1

        largest_area = max(largest_area, w * h)

print(largest_area)
