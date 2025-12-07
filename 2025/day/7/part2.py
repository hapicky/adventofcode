from sys import stdin

# input diagram
rows = []
start_x = None

for line in stdin:
    row = line.rstrip()
    if 'S' in row:
        start_x = row.index('S')

    rows.append(row)

# dp[y][x] = number of timelines that reach (x, y)
WIDTH = len(rows[0])
dp = [[0] * WIDTH for _ in range(len(rows))]
dp[1][start_x] = 1

for y in range(1, len(rows) - 1):
    for x in range(WIDTH):
        if rows[y][x] == '^':
            dp[y+1][x-1] += dp[y][x]
            dp[y+1][x+1] += dp[y][x]
        else:
            dp[y+1][x] += dp[y][x]

total_timelines = sum(dp[-1])
print(total_timelines)
