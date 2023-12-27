from sys import stdin

# 入力
rows = []
for y, line in enumerate(stdin):
    row = list(line.rstrip())
    rows.append(row)

    # スタート地点の特定
    if 'S' in row:
        sx = row.index('S')
        sy = y

upper_joints = ['|', '7', 'F', 'S']
left_joints = ['-', 'L', 'F', 'S']

# 隙間ができるように各行各列の間に挿入する
# 行
t = len(rows) + 1
for i in range(t):
    row = [' '] * len(rows[0])
    y = i * 2

    if y == 0:
        rows.insert(y, row)
        continue

    for x in range(len(row)):
        if rows[y-1][x] in upper_joints:
            row[x] = '|'

    rows.insert(y, row)

# 列
t = len(rows[0]) + 1
for row in rows:
    for i in range(t):
        x = i * 2
        col = ' '

        if x > 0 and row[x-1] in left_joints:
            col = '-'
        
        row.insert(x, col)

# スタート地点の調整
sx = sx * 2 + 1
sy = sy * 2 + 1

# for row in rows:
#     print(''.join(row))

width = len(rows[0])
height = len(rows)

# 訪問済
visited = [[False] * width for _ in range(height)]

# 各方向のx, y増分
directions = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0),
}

# 自身から見てつながる相手
joints = {
    '|': {
        'up': ['|', '7', 'F', 'S'],
        'down': ['|', 'L', 'J', 'S'],
    },
    '-': {
        'left': ['-', 'L', 'F', 'S'],
        'right': ['-', 'J', '7', 'S'],
    },
    'L': {
        'up': ['|', '7', 'F', 'S'],
        'right': ['-', 'J', '7', 'S'],
    },
    'J': {
        'up': ['|', '7', 'F', 'S'],
        'left': ['-', 'L', 'F', 'S'],
    },
    '7': {
        'down': ['|', 'L', 'J', 'S'],
        'left': ['-', 'L', 'F', 'S'],
    },
    'F': {
        'down': ['|', 'L', 'J', 'S'],
        'right': ['-', 'J', '7', 'S'],
    },
    'S': {
        'up': ['|', '7', 'F'],
        'down': ['|', 'L', 'J'],
        'left': ['-', 'L', 'F'],
        'right': ['-', 'J', '7'],
    },
}

q = []

# ループ上を訪問
def visit_on_the_loop(x, y):
    joint = joints[rows[y][x]]

    # 自身がつながる各方向を見る
    for dir in joint.keys():
        px, py = directions[dir]
        nx = x + px
        ny = y + py

        if nx < 0 or width <= nx or ny < 0 or height <= ny:
            continue

        if visited[ny][nx]:
            continue

        # 行先がつながる相手なら訪問
        if rows[ny][nx] in joint[dir]:
            visited[ny][nx] = True
            q.append((nx, ny))


# スタート地点からループ上を訪問する
visited[sy][sx] = True
q.append((sx, sy))

while len(q) > 0:
    x, y = q.pop(0)
    visit_on_the_loop(x, y)


# ループ上にないジャンクパイプは「.」に置き換える
for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col != ' ' and col != '.' and not visited[y][x]:
            if y % 2 == 0 or x % 2 == 0:
                # ただし隙間を開けるために挿入した箇所は空白にする
                rows[y][x] = ' '
            else:
                rows[y][x] = '.'

# 外側を訪問
def visit_outside(x, y):
    # 訪問された「.」は空白にしておく（外側から到達可能）
    if rows[y][x] == '.':
        rows[y][x] = ' '

    for px, py in directions.values():
        nx = x + px
        ny = y + py

        if nx < 0 or width <= nx or ny < 0 or height <= ny:
            continue

        if visited[ny][nx]:
            continue

        if rows[ny][nx] != ' ' and rows[ny][nx] != '.':
            continue

        visited[ny][nx] = True
        q.append((nx, ny))


visited[0][0] = True
q.append((0, 0))

while len(q) > 0:
    x, y = q.pop(0)
    visit_outside(x, y)

ans = 0
for row in rows:
    # print(''.join(row))
    ans += row.count('.')

print(ans)
