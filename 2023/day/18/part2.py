from sys import stdin

# 入力
plans = []

dirs = ['R', 'D', 'L', 'U']
for line in stdin:
    _, digits = line.rstrip().split('#')
    meter = int(''.join(digits[0:5]), 16)
    dir = dirs[int(digits[5])]
    plans.append((dir, meter))

# FIXME: 以下part1のやり方だとメモリも計算量も膨大になってしまう
exit(1)

# 仮の広さ
TMP_SIZE = 10000000
rows = [[0] * TMP_SIZE for _ in range(TMP_SIZE)]
# 中心からスタート
OFFSET = TMP_SIZE // 2
rows[0+OFFSET][0+OFFSET] = 1
cur = (0+OFFSET, 0+OFFSET)

# 各方向のx, y増分
px_py = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

# 最も左の塹壕
most_left_points = [(float('inf'), 0)]

# 塹壕の箇所を記録
for plan in plans:
    dir = plan[0]
    px, py = px_py[dir]
    meter = plan[1]

    for _ in range(meter):
        cur = (cur[0]+px, cur[1]+py)
        rows[cur[1]][cur[0]] = 1

        # 最も左の塹壕を記録
        most_left_point = most_left_points[0]
        if cur[0] == most_left_point[0]:
            most_left_points.append(cur)
        elif cur[0] < most_left_point[0]:
            most_left_points = [cur]

# for row in rows:
#     print(','.join(map(str, row)))

# 塹壕の内側の位置を特定
for x, y in most_left_points:
    if rows[y][x+1] == 0:
        start = (x+1, y)
        break

# 訪問したか否か
visited = [[False] * TMP_SIZE for _ in range(TMP_SIZE)]

# 塹壕の内側を掘っていく
def visit(x, y):
    next_points = []

    if rows[y][x] == 1:
        return next_points

    if visited[y][x]:
        return next_points

    rows[y][x] = 1
    visited[y][x] = True

    for px, py in px_py.values():
        nx = x + px
        ny = y + py
        next_points.append((nx, ny))
    
    return next_points


q = [start]
while len(q) > 0:
    x, y = q.pop(0)
    next_points = visit(x, y)
    for np in next_points:
        q.append(np)

# for row in rows:
#     print(','.join(map(str, row)))

# 集計
ans = 0
for y in range(TMP_SIZE):
    ans += sum(rows[y])

print(ans)
