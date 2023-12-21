from sys import stdin

rows = []
start_x = -1
start_y = -1

for y, line in enumerate(stdin):
    row = list(line.rstrip())
    rows.append(row)

    if start_x < 0:
        start_x = line.find('S')
        if start_x >= 0:
            start_y = y

width = len(rows[0])
height = len(rows)

# start_x, start_y どちらも65
# width, height どちらも131
# スタート地点の上下左右に岩（#）はない
# このことから以下が言える

# ひとつ上の地図に最短66歩で行くことができる
# 最大202300枚上の地図に行くことができる ceil((26501365 - (66 - 1)) / 131)
# 最短距離で最も上の地図に移動した場合、その地点は(65, 130)で残り130歩 (26501365 - 66) % 131

# ひとつ右の地図に最短66歩で行くことができる
# 最大202300枚右の地図に行くことができる
# 最短距離で最も上の地図に移動した場合、その地点は(0, 65)で残り130歩

# ひとつ下の地図に最短66歩で行くことができる
# 最大202300枚下の地図に行くことができる
# 最短距離で最も下の地図に移動した場合、その地点は(65, 0)で残り130歩

# ひとつ左の地図に最短66歩で行くことができる
# 最大202300枚左の地図に行くことができる
# 最短距離で最も左の地図に移動した場合、その地点は(130, 65)で残り130歩

# 右上の地図に移動した場合、その地点は(0, 130)で残り64歩 (26501365 - (66 + 66)) % 131
# 右下の地図に移動した場合、その地点は(0, 0)で残り64歩
# 左下の地図に移動した場合、その地点は(130, 0)で残り64歩
# 左上の地図に移動した場合、その地点は(130, 130)で残り64歩


# 各方向のx, y増分
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

# (sx, sy) からスタートしてmax_steps歩で到達できる箇所の数を返す
def count_plot(sx, sy, max_steps):
    # 訪問済
    visited = [[False] * width for _ in range(height)]
    # 最終地点になりうる箇所に1を設定
    goals = [[0] * width for _ in range(height)]

    q = []

    # 訪問
    def visit(x, y, steps, max_steps):
        # 奇数歩で行ける場合はカウント
        if steps % 2 == 1:
            goals[y][x] = 1
        
        if steps == max_steps:
            return

        for px, py in directions:
            nx = x + px
            ny = y + py
            
            if nx < 0 or width <= nx or ny < 0 or height <= ny:
                continue

            if rows[ny][nx] == '#':
                continue

            if visited[ny][nx]:
                continue

            # 何度も判定しないように、キューに入れる前に訪問済にする
            visited[ny][nx] = True
            q.append((nx, ny, steps+1))

    # キューにスタート地点を入れる
    visited[sy][sx] = True
    q.append((sx, sy, 0))

    while len(q) > 0:
        x, y, steps = q.pop(0)
        visit(x, y, steps, max_steps)

        if steps > max_steps:
            break
    
    # 集計
    ret = 0
    for g in goals:
        ret += sum(g)
        # print(''.join(map(str, g)))

    return ret


# 地図全体を巡回した場合の数（129歩から増えない）
full_count = count_plot(start_x, start_y, 131)
print(full_count)

# 上
upper_count = count_plot(65, 130, 130)
print(upper_count)
# 右
right_count = count_plot(0, 65, 130)
print(right_count)
# 下
lower_count = count_plot(65, 0, 130)
print(lower_count)
# 左
left_count = count_plot(130, 65, 130)
print(left_count)

# 右上
upper_right_count = count_plot(0, 130, 64)
print(upper_right_count)
# 右下
lower_right_count = count_plot(0, 0, 64)
print(lower_right_count)
# 左下
lower_left_count = count_plot(130, 0, 64)
print(lower_left_count)
# 左上
upper_left_count = count_plot(130, 130, 64)
print(upper_left_count)

# 集計
ans = 0
# 上下左右の端
ans += upper_count
ans += right_count
ans += lower_count
ans += left_count
# 右上・右下・左下・左上
ans += upper_right_count * (202300 - 1)
ans += lower_right_count * (202300 - 1)
ans += lower_left_count * (202300 - 1)
ans += upper_left_count * (202300 - 1)
# 全体を巡回できる部分
ans += full_count * ((202300 * 202300 // 2) * 4 - (202300 * 2 - 1) - (202300 * 2 - 1) - 1)

# WA...（少ないらしい）
print(ans)
