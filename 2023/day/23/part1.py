from sys import stdin
from copy import deepcopy

# 入力
rows = []
for line in stdin:
    row = list(line.rstrip())
    rows.append(row)

width = len(rows[0])
height = len(rows)

# (x, y)までの最大歩数をmax_steps[y][x]とする
max_steps = [[0 for _ in range(width)] for _ in range(height)]

# 進行方向とx, yの増分
directions = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1)
}

next_directions = {
    '>': ['>', 'v', '^'],
    '<': ['<', 'v', '^'],
    'v': ['>', '<', 'v'],
    '^': ['>', '<', '^']
}

# 訪問済
visited = [[False for _ in range(width)] for _ in range(height)]
# スタート地点
visited[0][1] = True

def visit(dir, x, y, step, visited):
    max_steps[y][x] = max(max_steps[y][x], step)
    visited[y][x] = True

    # スロープだったら次の方向を限定
    if rows[y][x] in directions.keys():
        next_dirs = [rows[y][x]]
    else:
        next_dirs = next_directions[dir]

    path = 1
    for next_dir in next_dirs:
        px, py = directions[next_dir]
        nx = x + px
        ny = y + py

        if nx < 0 or width <= nx or ny < 0 or height <= ny:
            continue

        if rows[ny][nx] == '#':
            continue

        if visited[ny][nx]:
            continue

        if path > 1:
            # 広いと遅いので必要なとき（分岐する場合）だけディープコピー
            q.append((next_dir, nx, ny, step+1, deepcopy(visited)))
        else:
            q.append((next_dir, nx, ny, step+1, visited))
        
        path += 1


q = []
q.append(('v', 1, 1, 1, visited))

while len(q) > 0:
    dir, x, y, step, visited = q.pop(0)
    visit(dir, x, y, step, visited)

# 解答
ans = max_steps[height-1][width-2]
print(ans)
