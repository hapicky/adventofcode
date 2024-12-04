from sys import stdin

grid = []
for line in stdin:
    grid.append(list(line.rstrip('\n')))

H = len(grid)
W = len(grid[0])
MS = ['M', 'S']

ans = 0
for cy in range(1, H-1):
    for cx in range(1, W-1):
        if grid[cy][cx] != 'A':
            continue

        ms1 = sorted([grid[cy-1][cx-1], grid[cy+1][cx+1]])
        ms2 = sorted([grid[cy+1][cx-1], grid[cy-1][cx+1]])

        if ms1 == MS and ms2 == MS:
            ans += 1

print(ans)
