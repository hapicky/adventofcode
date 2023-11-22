from sys import stdin

cavern = []
width = 0

for line in stdin:
    width = len(line)
    cavern.append(line)

height = len(cavern)

# 上からy行目、左からx列目まで行く最小リスクをdp[y][x]とする
dp = [[float('inf')] * (width+1) for _ in range(height+1)]
dp[1][1] = 0

for y in range(1, height+1):
    for x in range(1, width+1):
        if y == 1 and x == 1:
            continue
        
        dp[y][x] = min(dp[y-1][x], dp[y][x-1]) + int(cavern[y-1][x-1])

ans = dp[height][width]
print(ans)
# なぜか正解と1違う値になったのだけど、なぜだろう？

