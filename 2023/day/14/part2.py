from sys import stdin

rows = []

# 入力
for line in stdin:
    row = list(line.rstrip())
    rows.append(row)

width = len(rows[0])
height = len(rows)

# x列、y行にいる場合に東西へ移動可能な場所。添え字は[y][x]
east_candidates = [[list() for _ in range(width)] for _ in range(height)]
west_candidates = [[list() for _ in range(width)] for _ in range(height)]
# x列、y行にいる場合に南北へ移動可能な場所。添え字は[x][y]
south_candidates = [[list() for _ in range(height)] for _ in range(width)]
north_candidates = [[list() for _ in range(height)] for _ in range(width)]

# 移動可能な場所を特定しておく
for y in range(height):
    for x in range(width):
        c = rows[y][x]

        if c == '#':
            # それよりも東側からの移動可能な場所を訂正
            west_candidates[y][x] = []
            for x2 in range(x+1, width):
                west_candidates[y][x2] = [cand for cand in west_candidates[y][x2] if cand > x2]

            # それよりも北側からの移動可能な場所を訂正
            north_candidates[x][y] = []
            for y2 in range(y+1, height):
                north_candidates[x][y2] = [cand for cand in north_candidates[x][y2] if cand > y2]

            continue

        # 西へ移動可能な場所として記録
        for x2 in range(x, width):
            west_candidates[y][x2].append(x)

        # 北へ移動可能な場所として記録
        for y2 in range(y, height):
            north_candidates[x][y2].append(y)

for y in range(height-1, -1, -1):
    for x in range(width-1, -1, -1):
        c = rows[y][x]

        if c == '#':
            # それよりも西側からの移動可能な場所を訂正
            east_candidates[y][x] = []
            for x2 in range(x):
                east_candidates[y][x2] = [cand for cand in east_candidates[y][x2] if cand < x]

            # それよりも南側からの移動可能な場所を訂正
            south_candidates[x][y] = []
            for y2 in range(y):
                south_candidates[x][y2] = [cand for cand in south_candidates[x][y2] if cand < y]

            continue

        # 東へ移動可能な場所として記録
        for x2 in range(x+1):
            east_candidates[y][x2].append(x)

        # 南へ移動可能な場所として記録
        for y2 in range(y+1):
            south_candidates[x][y2].append(y)

for _ in range(1000000000):
    # north
    for x in range(width):
        used = set()
        for y in range(height):
            if y == 0:
                continue

            if rows[y][x] != 'O':
                continue

            candidates = north_candidates[x][y]
            for y2 in candidates:
                if y2 not in used:
                    rows[y][x] = '.'
                    rows[y2][x] = 'O'
                    used.add(y2)
                    break

    # west
    for y in range(height):
        used = set()
        for x in range(width):
            if x == 0:
                continue

            if rows[y][x] != 'O':
                continue

            candidates = west_candidates[y][x]
            for x2 in candidates:
                if x2 not in used:
                    rows[y][x] = '.'
                    rows[y][x2] = 'O'
                    used.add(x2)
                    break

    # south
    for x in range(width):
        used = set()
        for y in range(height-2, -1, -1):
            if rows[y][x] != 'O':
                continue

            candidates = south_candidates[x][y]
            for y2 in candidates:
                if y2 not in used:
                    rows[y][x] = '.'
                    rows[y2][x] = 'O'
                    used.add(y2)
                    break

    # east
    for y in range(height):
        used = set()
        for x in range(width-2, -1, -1):
            if rows[y][x] != 'O':
                continue

            candidates = east_candidates[y][x]
            for x2 in candidates:
                if x2 not in used:
                    rows[y][x] = '.'
                    rows[y][x2] = 'O'
                    used.add(x2)
                    break


for row in rows:
    print(row)


ans = 0
for y, row in enumerate(rows):
    for c in row:
        if c == 'O':
            ans += height - y

print(ans)