from sys import stdin

def match(expected, values):
    # ビット全探索
    for i in range(pow(2, len(values) - 1)):
        tmp = values[0]
        b = 1

        for j in range(len(values) - 1):
            if i & b == 0:
                tmp += values[j+1]
            else:
                tmp *= values[j+1]

            b <<= 1
        
        if tmp == expected:
            return True

    return False

ans = 0
for line in stdin:
    l, r = line.split(':')

    expected = int(l)
    values = list(map(int, r.split()))

    if match(expected, values):
        ans += expected

print(ans)
