from sys import stdin

rows = []

# 入力
for line in stdin:
    rows.append(list(line.rstrip()))

width = len(rows[0])
height = len(rows)

for _ in range(1000000000):
    # north
    for x in range(width):
        for y in range(height):
            if y == 0:
                continue

            if rows[y][x] != 'O':
                continue

            # 行けるだけ移動
            moved = y
            for y2 in range(y, 0, -1):
                if rows[y2-1][x] != '.':
                    break

                moved = y2 - 1
            
            rows[y][x] = '.'
            rows[moved][x] = 'O'

    # west
    for y in range(height):
        for x in range(width):
            if x == 0:
                continue

            if rows[y][x] != 'O':
                continue

            # 行けるだけ移動
            moved = x
            for x2 in range(x, 0, -1):
                if rows[y][x2-1] != '.':
                    break

                moved = x2 - 1
            
            rows[y][x] = '.'
            rows[y][moved] = 'O'

    # south
    for x in range(width):
        for y in range(height-2, -1, -1):
            if rows[y][x] != 'O':
                continue

            # 行けるだけ移動
            moved = y
            for y2 in range(y, height-1):
                if rows[y2+1][x] != '.':
                    break

                moved = y2 + 1
            
            rows[y][x] = '.'
            rows[moved][x] = 'O'

    # east
    for y in range(height):
        for x in range(width-2, -1, -1):
            if rows[y][x] != 'O':
                continue

            # 行けるだけ移動
            moved = x
            for x2 in range(x, width-1):
                if rows[y][x2+1] != '.':
                    break

                moved = x2 + 1
            
            rows[y][x] = '.'
            rows[y][moved] = 'O'


ans = 0
for y, row in enumerate(rows):
    for c in row:
        if c == 'O':
            ans += height - y

print(ans)