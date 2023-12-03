from sys import stdin
from collections import defaultdict

i = 1

# i行目、j列目にある数値nを(i, j, n)として収集する
numbers = []

# *がある箇所にその位置を設定する二次元配列
SIZE = 140
stars = [[None] * (SIZE+2) for _ in range(SIZE+2)]

for line in stdin:
    # 検出された数字
    tmp_number = ''
    # 開始位置
    start_pos = 0

    # 末尾の数字を処理するために（改行を除いてから）ピリオドを追加して処理
    for j, c in enumerate(line.rstrip() + '.'):
        if c.isnumeric():
            if tmp_number == '':
                # 先頭の数字
                start_pos = j + 1
                tmp_number = c
            else:
                # 後続の数字
                tmp_number += c
        else:
            if tmp_number != '':
                # 数字以外で、その前に数字があった場合は数字の位置と値を収集
                numbers.append((i, start_pos, int(tmp_number)))
                tmp_number = ''
            
            if c == '*':
                # *の位置を記録
                stars[i][j+1] = (i, j+1)
    
    i += 1

# *に隣接する数値
numbers_for_star = defaultdict(list)

for i, j, n in numbers:
    l = len(str(n))
    # 周辺にある*を探す
    for si in range(i-1, i+2):
        for star in stars[si][j-1:j+l+1]:
            if star is not None:
                numbers_for_star[star].append(n)

ans = 0
for k, v in numbers_for_star.items():
    if len(v) > 1:
        ans += v[0] * v[1]

print(ans)
