from sys import stdin
import re

ans = 0
for line in stdin:
    for x, y in re.findall('mul\((\d+),(\d+)\)', line):
        ans += int(x) * int(y)

print(ans)
