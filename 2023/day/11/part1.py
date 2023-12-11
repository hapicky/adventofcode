from sys import stdin
from itertools import combinations

# 行・列の拡張
row_expansions = []
col_expansions = []

# 銀河
galaxies = []

width = 0
height = 0

# 入力の読み取り
for y, line in enumerate(stdin):
    height += 1
    if y == 0:
        width = len(line) - 1
        col_expansions = [1] * width
    
    galaxy_found = False

    for x, c in enumerate(line.rstrip()):
        if c == '#':
            col_expansions[x] = 0
            galaxy_found = True
            galaxies.append((x, y))
    
    if galaxy_found:
        row_expansions.append(0)
    else:
        row_expansions.append(1)

# 行・列の拡張の累積和を取っておく
row_expansions_sum = [0] * height
col_expansions_sum = [0] * width

prev = 0
for y in range(height):
    row_expansions_sum[y] = prev + row_expansions[y]
    prev = row_expansions_sum[y]

prev = 0
for x in range(height):
    col_expansions_sum[x] = prev + col_expansions[x]
    prev = col_expansions_sum[x]

# 総距離を算出
ans = 0
for g1, g2 in combinations(galaxies, 2):
    x1, x2 = sorted([g1[0], g2[0]])
    y1, y2 = sorted([g1[1], g2[1]])

    # 間の拡張を算出
    if x2 == 0:
        col_expansion = 0
    else:
        col_expansion = col_expansions_sum[x2-1] - col_expansions_sum[x1]

    if y2 == 0:
        row_expansion = 0
    else:
        row_expansion = row_expansions_sum[y2-1] - row_expansions_sum[y1]

    # 距離
    distance = x2 - x1 + y2 - y1 + col_expansion + row_expansion
    ans += distance

print(ans)