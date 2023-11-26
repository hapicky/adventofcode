import sys

sys.setrecursionlimit(10**9)

cavern = []
width = 0

for line in sys.stdin:
    width = len(line)
    cavern.append(line)

height = len(cavern)

# 上からy行目、左からx列目まで行く最小リスクをmin_risks[y-1][x-1]とする
min_risks = [[float('inf')] * width for _ in range(height)]
min_risks[0][0] = 0

def visit(y, x, cur_risk):
    neighbors = []

    # 右
    if x < width - 1:
        neighbors.append((y, x+1))

    # 下
    if y < height - 1:
        neighbors.append((y+1, x))

    # 左
    if x > 1:
        neighbors.append((y, x-1))
    
    # 上
    if y > 1:
        neighbors.append((y-1, x))
    
    for ny, nx in neighbors:
        risk = int(cavern[ny][nx])
        sum_risk = cur_risk + risk
        if sum_risk < min_risks[ny][nx]:
            min_risks[ny][nx] = sum_risk
            visit(ny, nx, sum_risk)

visit(0, 0, 0)

ans = min_risks[height-1][width-1]
print(ans)
