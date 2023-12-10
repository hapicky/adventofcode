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

visited = defaultdict(bool)
# 各行、各列でループ上にある場合はTrue
on_the_loop_row = [[False] * (width+2) for _ in range(height+2)]
on_the_loop_col = [[False] * (height+2) for _ in range(width+2)]

def visit(point):
    visited[point] = True
    # 各行、各列でループ上にある位置にTrueをマークする
    on_the_loop_row[point[1]][point[0]] = True
    on_the_loop_col[point[0]][point[1]] = True

    for nex in routes[point]:
        if not visited[nex]:
            visit(nex)

visit(start)

ans = 0
for y in range(1, height+1):
    for x in range(1, width+1):
        c = tiles[y][x]
        if c != '.':
            continue
        
        left_pipe_mod = sum(on_the_loop_row[y][:x]) % 2
        right_pipe_mod = sum(on_the_loop_row[y][x+1:]) % 2
        upper_pipe_mod = sum(on_the_loop_col[x][:y]) % 2
        lower_pipe_mod = sum(on_the_loop_col[x][y+1:]) % 2

        # 外側にあるパイプが奇数であれば内側？と思ったが違うようだ
        if left_pipe_mod == 1 and right_pipe_mod == 1 and upper_pipe_mod == 1 and lower_pipe_mod == 1:
            ans += 1

print(ans)
