from collections import deque
import sys

# 地図（入力）
cavern = []
for line in sys.stdin:
    row = list(map(int, line.rstrip()))
    cavern.append(row)

height = len(cavern)
width = len(cavern[0])

# 実際の地図（5倍）
TIMES = 5
full_height = height * TIMES
full_width = width * TIMES
full_cavern = [[0] * full_width for _ in range(full_height)]

for ty in range(TIMES):
    for ny in range(height):
        for tx in range(TIMES):
            if ty == 0 and tx == 0:
                # 左上は地図と同じ値
                values = cavern[ny]
            else:
                if tx == 0:
                    # 左端の場合は一つ上の段に、
                    prev_values = full_cavern[height * (ty-1) + ny][0:width]
                else:
                    # そうでなれば左隣りの値に、
                    prev_values = full_cavern[height * ty + ny][width * (tx-1):width * tx]

                # 1を加えた値
                values = [(v % 9 + 1) for v in prev_values]
            
            full_cavern[height * ty + ny][width * tx:width * (tx+1)] = values

# for c in full_cavern:
#     print(c)


# 上からy行目、左からx列目まで行く最小リスクをmin_risks[y-1][x-1]とする
min_risks = [[float('inf')] * full_width for _ in range(full_height)]
min_risks[0][0] = 0

q = deque()

def visit(y, x, cur_risk):
    neighbors = []

    # 右
    if x < full_width - 1:
        neighbors.append((y, x+1))

    # 下
    if y < full_height - 1:
        neighbors.append((y+1, x))

    # 左
    if x > 1:
        neighbors.append((y, x-1))
    
    # 上
    if y > 1:
        neighbors.append((y-1, x))
    
    next_visits = []

    for ny, nx in neighbors:
        risk = full_cavern[ny][nx]
        sum_risk = cur_risk + risk
        if sum_risk < min_risks[ny][nx]:
            min_risks[ny][nx] = sum_risk
            next_visits.append((ny, nx, sum_risk))
    
    return next_visits


q.append((0, 0, 0))

while len(q) > 0:
    y, x, cur_risk = q.popleft()

    next_visits = visit(y, x, cur_risk)
    for n in next_visits:
        q.append(n)

ans = min_risks[full_height-1][full_width-1]
print(ans)
