from sys import stdin

grid = []
for line in stdin:
    grid.append(list(line.rstrip('\n')))

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
]

H = len(grid)
W = len(grid[0])

ans = 0
for sy in range(len(grid)):
    for sx in [i for i, c in enumerate(grid[sy]) if c == 'X']:
        for px, py in directions:
            x = sx
            y = sy
            valid = True

            for expected in 'MAS':
                x += px
                y += py
                if x < 0 or y < 0 or W <= x or H <= y:
                    valid = False
                    break

                if grid[y][x] != expected:
                    valid = False
                    break
            
            if valid:
                ans += 1

print(ans)
