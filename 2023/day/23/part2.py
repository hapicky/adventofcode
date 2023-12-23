from sys import stdin
from copy import deepcopy
from collections import defaultdict

# 入力
rows = []
for line in stdin:
    row = list(line.rstrip())
    rows.append(row)

width = len(rows[0])
height = len(rows)

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

# 分岐地点
junctions = set()
# 始点と終点を追加
junctions.add((1, 0))
junctions.add((width-2, height-1))

# 分岐を特定
for y in range(height):
    for x in range(width):
        if rows[y][x] == '#':
            continue
    
        path = 0
        for px, py in directions.values():
            nx = x + px
            ny = y + py

            if nx < 0 or width <= nx or ny < 0 or height <= ny:
                continue

            if rows[ny][nx] != '#':
                path += 1
    
        if path > 2:
            junctions.add((x, y))

# 訪問済
visited = [[False for _ in range(width)] for _ in range(height)]
# スタート地点
visited[0][1] = True

# 分岐から分岐までの距離
distance = defaultdict(dict)

def visit(dir, x, y, step, visited, prev_junction):
    visited[y][x] = True

    for next_dir in next_directions[dir]:
        # print((x, y), next_dir)
        px, py = directions[next_dir]
        nx = x + px
        ny = y + py

        if nx < 0 or width <= nx or ny < 0 or height <= ny:
            continue

        if rows[ny][nx] == '#':
            continue

        # 次の位置が分岐の場合、そこまでの距離をメモ
        next_p = (nx, ny)
        if next_p in junctions:
            d = step + 1
            if next_p in distance[prev_junction]:
                # 分岐から分岐までの行き方が複数ある場合は長い方を採用
                distance[prev_junction][next_p] = max(distance[prev_junction][next_p], d)
            else:
                distance[prev_junction][next_p] = d
            
        if visited[ny][nx]:
            continue

        if (x, y) in junctions:
            # ここでvisitedをdeepcopyして渡さないと全部のルートを探索してくれない。なんでだ？
            q.append((next_dir, nx, ny, 1, visited, (x, y)))
        else:
            q.append((next_dir, nx, ny, step+1, visited, prev_junction))


q = []
q.append(('v', 1, 1, 1, visited, (1, 0)))

while len(q) > 0:
    dir, x, y, step, visited, prev_junction = q.pop(0)
    visit(dir, x, y, step, visited, prev_junction)

for p_1, d in distance.items():
    for p_2, dist in d.items():
        print(p_1, p_2, dist)


# TODO 各分岐間の距離が求められたら、そのうち最も距離の長い順路を特定する
