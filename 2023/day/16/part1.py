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

# ビームが通過したか否か
energized = [[False] * width for _ in range(height)]

# 各方向で訪問済か
visited = [[defaultdict(bool) for _ in range(width)] for _ in range(height)]

# キュー
q = []
heapq.heapify(q)

# x, yのマスにdir方向で訪問する
def visit(x, y, dir):
    # 範囲外
    if x < 0 or width <= x or y < 0 or height <= y:
        return

    # 訪問済
    if visited[y][x][dir] == True:
        return

    visited[y][x][dir] = True

    energized[y][x] = True
    tile = rows[y][x]
    next_dirs = directions[tile][dir]

    for next_dir in next_dirs:
        px, py = px_py[next_dir]
        heapq.heappush(q, (x+px, y+py, next_dir))

# 左上からスタート
heapq.heappush(q, (0, 0, 'right'))

# キューがなくなるまで訪問
while len(q) > 0:
    x, y, frm = heapq.heappop(q)
    visit(x, y, frm)

# 集計
ans = 0
for e in energized:
    ans += sum(e)

print(ans)
