from sys import stdin

l_values = []
r_values = []

for line in stdin:
    l, r = map(int, line.split())
    l_values.append(l)
    r_values.append(r)

l_values.sort()
r_values.sort()

ans = 0
for i in range(len(l_values)):
    ans += abs(l_values[i] - r_values[i])

print(ans)
