from sys import stdin
import re

ans = 0
enabled = True
for line in stdin:
    for part in re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
        if part == 'do()':
            enabled = True
        elif part == "don't()":
            enabled = False
        elif enabled:
            m = re.match(r'mul\((\d+),(\d+)\)', part)
            x, y = m.group(1, 2)
            ans += int(x) * int(y)

print(ans)
