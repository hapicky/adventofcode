from sys import stdin
from itertools import product

def match(expected, values):
    for operators in product(range(3), repeat=len(values) - 1):
        tmp = values[0]

        for j, operator in enumerate(operators):
            if operator == 0:
                tmp += values[j+1]
            elif operator == 1:
                tmp *= values[j+1]
            else:
                tmp = int(str(tmp) + str(values[j+1]))

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
