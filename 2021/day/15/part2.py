from sys import stdin

# 地図（入力）
cavern = []
for line in stdin:
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


# 上からy行目、左からx列目まで行く最小リスクをdp[y][x]とする
dp = [[float('inf')] * (full_width+1) for _ in range(full_height+1)]
dp[1][1] = 0

for y in range(1, full_height+1):
    for x in range(1, full_width+1):
        if y == 1 and x == 1:
            continue
        
        dp[y][x] = min(dp[y-1][x], dp[y][x-1]) + full_cavern[y-1][x-1]

ans = dp[full_height][full_width]
print(ans)
# part1と同じく正解にならない。なぜだろう？
