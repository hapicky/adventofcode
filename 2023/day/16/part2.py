from sys import stdin
from collections import defaultdict
import heapq

rows = []

# 入力
for line in stdin:
    row = list(line.rstrip())
    rows.append(row)

width = len(rows[0])
height = len(rows)

# 各タイルが、入ってきた向きに対してビームをどちらに向けるか
directions = {
    '.': {
        'up': ['up'],
        'down': ['down'],
        'left': ['left'],
        'right': ['right'],
    },
    '/': {
        'up': ['right'],
        'down': ['left'],
        'left': ['down'],
        'right': ['up'],
    },
    '\\': {
        'up': ['left'],
        'down': ['right'],
        'left': ['up'],
        'right': ['down'],
    },
    '|': {
        'up': ['up'],
        'down': ['down'],
        'left': ['up', 'down'],
        'right': ['up', 'down'],
    },
    '-': {
        'up': ['left', 'right'],
        'down': ['left', 'right'],
        'left': ['left'],
        'right': ['right'],
    },
}

# 各向きのx,y増分
px_py = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0),
}

configurations = []
configurations.extend([(0, y, 'right') for y in range(height)])
configurations.extend([(width-1, y, 'left') for y in range(height)])
configurations.extend([(x, 0, 'down') for x in range(width)])
configurations.extend([(x, height-1, 'up') for x in range(width)])

# x, yのマスにdir方向で訪問する
def visit(x, y, dir):
    # 範囲外
    if x < 0 or width <= x or y < 0 or height <= y:
        return

    # 訪問済
    global visited
    if visited[y][x][dir] == True:
        return

    visited[y][x][dir] = True

    global energized
    energized[y][x] = True
    tile = rows[y][x]
    next_dirs = directions[tile][dir]

    global q
    for next_dir in next_dirs:
        px, py = px_py[next_dir]
        heapq.heappush(q, (x+px, y+py, next_dir))

ans = 0
for sx, sy, sdir in configurations:
    # ビームが通過したか否か
    energized = [[False] * width for _ in range(height)]

    # 各方向で訪問済か
    visited = [[defaultdict(bool) for _ in range(width)] for _ in range(height)]

    # キュー
    q = []
    heapq.heapify(q)

    # スタート
    heapq.heappush(q, (sx, sy, sdir))

    # キューがなくなるまで訪問
    while len(q) > 0:
        x, y, frm = heapq.heappop(q)
        visit(x, y, frm)

    # 集計
    tmp_ans = 0
    for e in energized:
        tmp_ans += sum(e)
    
    ans = max(ans, tmp_ans)


print(ans)
