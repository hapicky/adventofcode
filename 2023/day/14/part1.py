from sys import stdin

cols = []

# 入力
for line in stdin:
    cells = list(line.rstrip())
    if not cols:
        cols = [list() for _ in range(len(cells))]
    
    for i, c in enumerate(cells):
        cols[i].append(c)

# 行数
rows = len(cols[0])

# 重さ
loads = [[0] * len(cols) for _ in range(rows)]

for c, col in enumerate(cols):
    for r in range(rows):
        if col[r] == 'O':
            # 北に行けるだけ移動
            r_moved = r
            for r2 in range(r, 0, -1):
                if col[r2-1] == '#':
                    break

                if loads[r2-1][c] > 0:
                    break
                
                r_moved = r2 - 1
            
            # 重さを記録
            loads[r_moved][c] = rows - r_moved

# 重さを合計
ans = 0
for load in loads:
    ans += sum(load)

print(ans)
