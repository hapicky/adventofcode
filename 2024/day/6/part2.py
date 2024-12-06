from sys import stdin

# 地図と開始位置の入力
rows = []
sx = None
sy = None

for i, line in enumerate(stdin):
    row = list(line.rstrip('\n'))
    rows.append(row)

    if row.count('^'):
        sx = row.index('^')
        sy = i

# 広さと訪問状態
H = len(rows)
W = len(rows[0])
visited = [[False] * W for _ in range(H)]
visited[sy][sx] = True

# 方向
directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

# 外に出るまで移動
cur_dir = 0
x = sx
y = sy
while True:
    nx = x + directions[cur_dir][0]
    ny = y + directions[cur_dir][1]

    if nx < 0 or ny < 0 or nx >= W or ny >= H:
        break

    if rows[ny][nx] == '#':
        cur_dir = (cur_dir + 1) % len(directions)
    else:
        visited[ny][nx] = True
        x = nx
        y = ny

# 指定位置に障害物を置いてループするかどうか
def is_stuck(ox, oy):
    stuck = False
    rows[oy][ox] = '#'

    # 方向転換する位置と方向
    turn_points = set()

    cur_dir = 0
    x = sx
    y = sy
    while True:
        nx = x + directions[cur_dir][0]
        ny = y + directions[cur_dir][1]

        if nx < 0 or ny < 0 or nx >= W or ny >= H:
            break

        if rows[ny][nx] == '#':
            cur_dir = (cur_dir + 1) % len(directions)
            if (x, y, cur_dir) in turn_points:
                stuck = True
                break
            turn_points.add((x, y, cur_dir))
        else:
            x = nx
            y = ny

    rows[oy][ox] = '.'
    return stuck

ans = 0
for oy in range(H):
    for ox in range(W):
        if not visited[oy][ox]:
            continue

        if ox == sx and oy == sy:
            continue

        if is_stuck(ox, oy):
            ans += 1

print(ans)
