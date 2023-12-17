from sys import stdin
from collections import defaultdict

rows = []

for line in stdin:
    row = list(map(int, line.rstrip()))
    rows.append(row)

width = len(rows[0])
height = len(rows)

# min_loss[y][x] => (x, y)における最小ロス
min_loss = [[float('inf')] * width for _ in range(height)]
min_loss[0][0] = 0
# visited_start[(x, y)] => (x, y)を訪問済か否か
visited_start = defaultdict(bool)
visited_start[(0, 0)] = True

# キュー：座標FROM, 座標TO, 現在ロス、方向、訪問済
q = []

# 最初のキューを登録
q.append(((0, 0), (0, 1), 0, 'down', visited_start.copy()))
q.append(((0, 0), (0, 2), 0, 'down', visited_start.copy()))
q.append(((0, 0), (1, 0), 0, 'right', visited_start.copy()))
q.append(((0, 0), (2, 0), 0, 'right', visited_start.copy()))

# 各方向のx, y増分
px_py = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0),
}

def visit(point_from, point_to, cur_loss, dir, visited):
    # 方向のx, y増分
    px, py = px_py[dir]

    # 繰り返し数と次の方向
    if dir == 'up' or dir == 'down':
        n = abs(point_from[1] - point_to[1])
        next_dirs = ['left', 'right']
    else:
        n = abs(point_from[0] - point_to[0])
        next_dirs = ['up', 'down']

    loss = cur_loss
    for i in range(n):
        x = point_from[0] + px * (i + 1)
        y = point_from[1] + py * (i + 1)
        # ロスを加算
        loss += rows[y][x]
        # 訪問済を記録
        visited[(x, y)] = True

    # 最少ロスを更新
    min_loss[y][x] = min(min_loss[y][x], loss)

    for next_dir in next_dirs:
        px, py = px_py[next_dir]
        next_point_to = (point_to[0] + px, point_to[1] + py)
        for i in range(3):
            if next_point_to[0] < 0 or width <= next_point_to[0] or next_point_to[1] < 0 or height <= next_point_to[1]:
                break

            if visited[(next_point_to[0], next_point_to[1])] == True:
                continue

            q.append((point_to, next_point_to, loss, next_dir, visited.copy()))
            next_point_to = (next_point_to[0] + px, next_point_to[1] + py)

cnt = 0
while len(q) > 0:
    point_from, point_to, cur_loss, dir, visited = q.pop(0)
    visit(point_from, point_to, cur_loss, dir, visited)
    cnt += 1
    if cnt % 100 == 0:
        for l in min_loss:
            print(l)
        print('---')

print(min_loss[height-1][width-1])
