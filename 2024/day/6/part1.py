from sys import stdin

# 地図と開始位置の入力
rows = []
x = None
y = None

for i, line in enumerate(stdin):
    row = list(line.rstrip('\n'))
    rows.append(row)

    if row.count('^'):
        x = row.index('^')
        y = i

# 広さと訪問状態
H = len(rows)
W = len(rows[0])
visited = [[False] * W for _ in range(H)]
visited[y][x] = True

# 方向
directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]
cur_dir = 0

# 外に出るまで移動
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

# 答え
ans = sum([sum(v) for v in visited])
print(ans)
