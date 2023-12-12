from sys import stdin
import re

ans = 0
for line in stdin:
    row, damaged = line.rstrip().split()

    # 条件にマッチする正規表現
    reg = '\.*'
    reg += '\.+'.join(['#{' + n + '}' for n in damaged.split(',')])
    reg += '\.*'
    pattern = re.compile(reg)

    # ?の数に応じてビット全探索
    q = row.count('?')
    for i in range(2**q):
        s = row
        for j in range(q):
            # ビットが立っている箇所を「#」に置換
            c = '.'
            if (i >> j) & 1:
                c = '#'
            s = s.replace('?', c, 1)

        # マッチすればカウント        
        if pattern.fullmatch(s):
            ans += 1

print(ans)
