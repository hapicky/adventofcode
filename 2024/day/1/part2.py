from sys import stdin
from collections import defaultdict

l_values = []
r_values = defaultdict(int)

for line in stdin:
    l, r = map(int, line.split())
    l_values.append(l)
    r_values[r] += 1

ans = 0
for i in range(len(l_values)):
    count = r_values[l_values[i]]
    ans += l_values[i] * count

print(ans)
