from sys import stdin

# 集計
def summarize(rows, cols):
    score = 0

    # 行
    for upper_bottom_row in range(0, len(rows)-1):
        lower_top_row = upper_bottom_row + 1
        size = min(upper_bottom_row + 1, len(rows) - lower_top_row)
        upper = rows[upper_bottom_row-size+1:upper_bottom_row+1]
        upper.reverse()
        lower = rows[lower_top_row:lower_top_row+size]

        if upper == lower:
            score += (upper_bottom_row + 1) * 100
            break

    # 列
    for left_right_col in range(0, len(cols)-1):
        right_left_col = left_right_col + 1
        size = min(left_right_col + 1, len(cols) - right_left_col)
        left = cols[left_right_col-size+1:left_right_col+1]
        left.reverse()
        right = cols[right_left_col:right_left_col+size]

        if left == right:
            score += (left_right_col + 1)
            break

    return score

rows = []
cols = []

ans = 0
for line in stdin:
    l = line.rstrip()

    # 区切り：集計
    if len(l) == 0:
        ans += summarize(rows, cols)
        rows = []
        cols = []
        continue

    # 行
    rows.append(list(l))

    # 列
    if len(cols) == 0:
        cols = [list() for _ in range(len(l))]
    
    for i, c in enumerate(list(l)):
        cols[i].append(c)


ans += summarize(rows, cols)
print(ans)
