import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)

# 入力の読み込み
tiles = []
for line in sys.stdin:
    tiles.append(list(line.rstrip()))

# 幅と高さ
width = len(tiles[0])
height = len(tiles)

# 処理しやすいように上下左右を拡張
for tile in tiles:
    tile.insert(0, '.')
    tile.append('.')

tiles.insert(0, ['.'] * (width+2))
tiles.append(['.'] * (width+2))

# 自身から見てつながる相手
upper_joints = ['|', '7', 'F', 'S']
lower_joints = ['|', 'L', 'J', 'S']
right_joints = ['-', 'J', '7', 'S']
left_joints = ['-', 'L', 'F', 'S']

# 経路を探す
routes = defaultdict(list)
start = None

for y in range(1, height+1):
    for x in range(1, width+1):
        cur = (x, y)
        c = tiles[y][x]

        if c == '|':
            # 上
            if tiles[y-1][x] in upper_joints:
                routes[cur].append((x, y-1))
            # 下
            if tiles[y+1][x] in lower_joints:
                routes[cur].append((x, y+1))

        elif c == '-':
            # 右
            if tiles[y][x+1] in right_joints:
                routes[cur].append((x+1, y))
            # 左
            if tiles[y][x-1] in left_joints:
                routes[cur].append((x-1, y))

        elif c == 'L':
            # 上
            if tiles[y-1][x] in upper_joints:
                routes[cur].append((x, y-1))
            # 右
            if tiles[y][x+1] in right_joints:
                routes[cur].append((x+1, y))

        elif c == 'J':
            # 上
            if tiles[y-1][x] in upper_joints:
                routes[cur].append((x, y-1))
            # 左
            if tiles[y][x-1] in left_joints:
                routes[cur].append((x-1, y))

        elif c == '7':
            # 下
            if tiles[y+1][x] in lower_joints:
                routes[cur].append((x, y+1))
            # 左
            if tiles[y][x-1] in left_joints:
                routes[cur].append((x-1, y))

        elif c == 'F':
            # 右
            if tiles[y][x+1] in right_joints:
                routes[cur].append((x+1, y))
            # 下
            if tiles[y+1][x] in lower_joints:
                routes[cur].append((x, y+1))

        elif c == 'S':
            start = (x, y)
            # 上
            if tiles[y-1][x] in upper_joints:
                routes[cur].append((x, y-1))
            # 右
            if tiles[y][x+1] in right_joints:
                routes[cur].append((x+1, y))
            # 下
            if tiles[y+1][x] in lower_joints:
                routes[cur].append((x, y+1))
            # 左
            if tiles[y][x-1] in left_joints:
                routes[cur].append((x-1, y))

distance = 0
visited = defaultdict(bool)

def visit(point, cur_distance):
    visited[point] = True
    global distance
    distance = cur_distance
    for nex in routes[point]:
        if not visited[nex]:
            visit(nex, cur_distance+1)

visit(start, 0)
# この問題はループ前提なので全体距離の半分が最も遠い距離
ans = (distance+1) // 2
print(ans)
