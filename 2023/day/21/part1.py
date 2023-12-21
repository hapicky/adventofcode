from sys import stdin

# 訪問候補地
candidates = []

width = None

# 入力
for y, line in enumerate(stdin):
    row = list(line.rstrip())

    if width is None:
        width = len(row)
    
    candidates.append([True] * width)

    for x, c in enumerate(row):
        if c == '#':
            candidates[y][x] = False
        elif c == 'S':
            start_x = x
            start_y = y

height = len(candidates)


# 最終地点になりうる箇所に1を設定
goals = [[0] * width for _ in range(height)]

# 各方向のx, y増分
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

# 最大歩数
MAX_STEPS = 64

# 訪問
def visit(x, y, steps):
    # 偶数歩で行けるところは最終地点になりうる
    if steps % 2 == 0:
        goals[y][x] = 1
    
    if steps == MAX_STEPS:
        return
    
    for px, py in directions:
        nx = x + px
        ny = y + py
        
        if nx < 0 or width <= nx or ny < 0 or height <= ny:
            continue

        if not candidates[ny][nx]:
            continue

        # 何度も判定しないように、キューに入れる前に候補から外す
        candidates[ny][nx] = False
        q.append((nx, ny, steps+1))


# キューにスタート地点を入れる
q = []
candidates[start_y][start_x] = False
q.append((start_x, start_y, 0))

while len(q) > 0:
    x, y, steps = q.pop(0)
    visit(x, y, steps)


# 集計
ans = 0
for g in goals:
    ans += sum(g)

print(ans)
